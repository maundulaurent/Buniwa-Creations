from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class theBlog(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateField(default=timezone.now)
    blog_image = models.ImageField(upload_to='card_images/')
    author_image = models.ImageField(upload_to='author_images/')
    authors_comment = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog_details', kwargs={'pk': self.pk})
        # return reverse('tester', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name_plural = 'Blogs Section'

class blogComment(models.Model):
    post = models.ForeignKey(theBlog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True,related_name='replies', on_delete=models.CASCADE)#Added a parent for the replies
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.username} | {self.body[:50]} .."

class TextEntry(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]#display the first 50 characters in the admin area
    



        
class PortfolioPost(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=80)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    author_position = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    post_image = models.ImageField(upload_to='card_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    details_image = models.ImageField(upload_to='card_images/')
    client = models.CharField(max_length=50)
    portfolio_details_introduction = models.TextField()
    portfolio_details_description = models.TextField()
    project_created_at = models.DateTimeField()
    project_url = models.URLField(blank=True)


    def __str__(self):
        return self.title
    
    def get_portfolio_url(self):
        return reverse('portfolio_details', args=[str(self.id)])
    
    class Meta:
        verbose_name_plural = 'Portfolio Section'
    
class theTeam(models.Model):
    team_name = models.CharField(max_length=20)
    team_position = models.CharField(max_length=50)
    team_content = models.TextField()
    team_image = models.ImageField(upload_to='author_images/')
    team_twitter = models.URLField(blank=True)
    team_facebook = models.URLField(blank=True)
    team_intagram = models.URLField(blank=True)
    
    def __str__(self):
        return self.team_name
    
    class Meta:
        verbose_name_plural = 'Teams Section'


class theFaqs(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    
    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name_plural ='The FAQs'

class theTestimonials(models.Model):
    test_name = models.CharField(max_length=40)
    test_position = models.CharField(max_length=40)
    test_image = models.ImageField(upload_to='card_images/')
    test_quote = models.CharField(max_length=220)

    def __str__(self):
        return self.test_name
    
    class Meta:
        verbose_name_plural = 'Testimonials'

class theServices(models.Model):
    service_header = models.CharField(max_length=50)
    service_quote = models.TextField()
    service_image = models.ImageField(upload_to='card_images/')

    def __str__(self):
        return self.service_header
    
    class Meta:
        verbose_name_plural = 'Services'
