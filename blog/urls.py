from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('blog/', views.blog_list, name='blog-list'),
   path('blog/<slug:slug>/', views.blog_detail, name='blog-detail'),
]
