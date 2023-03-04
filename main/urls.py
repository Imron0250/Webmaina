from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('faq/', faq, name='faq'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('blog-single/<int:pk>/', blog_sing, name='blog_sing' ),
    path('save/', save, name="save")
]