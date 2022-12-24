from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('audit/', views.audit_list, name='audit-list'),
   path('audit/<slug:slug>', views.audit_detail, name='audit-detail'),
]
