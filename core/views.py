from django.shortcuts import render
from core.forms import ContactForm

# Create your views here.

def index(request):
    form = ContactForm
    context = {'form': form}
    return render(request, 'core/index.html', context)

def about(request):
    form = ContactForm
    context = {'form': form}
    return render(request, 'core/about.html', context)

def contact(request):
    form = ContactForm
    context = {'form': form}
    return render(request, 'core/contact.html', context)

def seo(request):
    form = ContactForm
    context = {'form': form}
    return render(request, 'services/seo.html', context)

def crm(request):
    form = ContactForm
    context = {'form': form}
    return render(request, 'services/crm.html', context)

def social(request):
    form = ContactForm
    context = {'form': form}
    return render(request, 'services/social.html', context)

def website(request):
    form = ContactForm
    context = {'form': form}
    return render(request, 'services/website.html', context)
