from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index' ),
    path('about',views.about, name='about' ),
    path('contact',views.contact, name='contact' ),
    path('services',views.services, name='services' ),
    path('blog',views.blog, name='blog' ),
    path('blogpost/<int:blog_id>',views.blogpost, name='blogpost' )
]