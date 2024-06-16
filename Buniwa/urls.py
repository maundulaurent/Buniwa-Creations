from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name = 'register'),
    path('signin', views.signin, name = 'signin'),
    path('about', views.about, name = 'about'),
    path('team', views.team, name = 'team'),
    path('services', views.services, name = 'services'),
    path('career', views.career, name = 'career'),
    path('contact', views.contact, name = 'contact'),
    path('projects', views.projects, name="projects"),
    path('faqs', views.faqs, name="faqs"),
    path('blog', views.blog, name="blog"),
    path('blog/<int:pk>/', views.blog_details, name="blog_details"),
    path('dash',views.dash, name="dash"),
    path('logout',views.user_logout, name='logout'),
    path('portfolio',views.portfolio, name="portfolio"),
    path('portfolio/<int:pk>/',views.portfolio_details, name="portfolio_details"),
    path('testimonial',views.testimonial, name="testimonial"),
    path('terms',views.terms, name="terms"),
    path('blog/<int:pk>/',views.blog_details, name="tester"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
