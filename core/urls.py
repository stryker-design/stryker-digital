from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('website', views.website, name='website'),
    path('social/', views.social, name='social'),
    path('crm/', views.crm, name='crm'),
    path('seo/', views.seo, name='seo'),
    path('deck/', views.pitch_deck, name='pitch-deck'),
]
