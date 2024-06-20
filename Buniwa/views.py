from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from .models import *
from .forms import *




# Create your views here.

def index(request):
    logos = theCompany.objects.all()
    return render(request, 'Buniwa/index.html', {'logos':logos})

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password1')

        if pass1!=pass2:
            return render(request, 'Buniwa/register', {'error': 'Passwords dont match'})
        else:
            my_user=User.objects.create_user(username=uname, email=email, password=pass1, first_name=first_name, last_name=last_name)
            my_user.save()
            return redirect('signin')

    return render(request, 'Buniwa/register.html')

def signin(request):        
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        
        user=authenticate(request, username=username, email=email, password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return redirect('signin')
    return render(request, 'Buniwa/signin.html')

def about(request):
    return render(request, 'Buniwa/about.html')

def team(request):
    cards = theTeam.objects.all()
    return render(request, 'Buniwa/team.html', {'cards': cards})

def services(request):
    service_items = theServices.objects.all()
    return render(request, 'Buniwa/services.html', {'service_items':service_items})

def career(request):
    return render(request, 'Buniwa/career.html')

# @login_required(login_url="signin")
def projects(request):
    return render(request, "Buniwa/projects.html")

def faqs(request):
    accordion_items = theFaqs.objects.all()
    return render(request, "Buniwa/faqs.html", {'accordion_items':accordion_items})


def blog(request):
    cards = theBlog.objects.all()
    return render(request, "Buniwa/blog.html", {'cards': cards})

def submit_text(request):
    if request.method == 'POST':
        form = TexTEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submit_text')
    else:
        form = TexTEntryForm()

    text_entries = TextEntry.objects.all()#retrieve all the entries in the TextEntry Model
    return render(request, 'Buniwa/submit_text.html', {'form': form, 'text_entries': text_entries})

def blog_details(request, pk):
    card = get_object_or_404(theBlog, pk=pk)
    if request.method == 'POST':
        form = blogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user#set the user to the currently logged in user
            comment.post = card#associate the comment with the current blog post
            parent_id = request.POST.get('parent_id')
            if parent_id:
                parent_comment = blogComment.objects.get(id=parent_id)
                comment.parent = parent_comment
            comment.save() #save the comment to the database
            return redirect('blog_details', pk=pk)
    else:
        form = blogCommentForm()
    blog_comments = blogComment.objects.filter(post=card, parent__isnull=True)
    total_comments = blog_comments.count()
    return render(request, "Buniwa/blog_details.html", {
    # return render(request, "Buniwa/tester.html", {
        'card': card,
        'blog_comments': blog_comments,
        'form': form,
        'total_comments': total_comments
        })


def dash(request):
    return render(request, "Buniwa/dash.html")

def user_logout(request):
    logout(request)
    return redirect('index')

def portfolio(request):
    cards = PortfolioPost.objects.all()
    return render(request, 'Buniwa/portfolio.html', {'cards': cards})

def portfolio_details(request, pk):
    card = get_object_or_404(PortfolioPost, pk=pk)
    return render(request, 'Buniwa/portfolio_details.html', {'card':card})


def testimonial(request):
    testimonial_items = theTestimonials.objects.all()
    return render(request, 'Buniwa/testimonial.html', {'testimonial_items':testimonial_items})

def terms(request):
    return render(request, 'Buniwa/terms.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

        # constructing the email

        subject = f"Contact Form Submission from {name}"
        message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        from_email = 'charlesmaundu16@gmail.com'
        recipient_list = ['charlesmaundu16@gmail.com']

        # sending the email

        send_mail(subject, message, from_email,recipient_list)

        messages.success(request, "Your message has been sent!")
        return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'Buniwa/contact.html', {'form': form})
    