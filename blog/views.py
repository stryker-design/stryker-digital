from django.shortcuts import render
from blog.models import BlogPost

# Create your views here.

def blog_list(request):
    blog = BlogPost.objects.all().order_by("-created_at").all()
    context = {'blog': blog}
    return render(request, 'blog/blog-list.html', context)

def blog_detail(request, slug):
    blog = BlogPost.objects.get(slug=slug)
    context = {'blog': blog}
    return render(request, 'blog/blog-detail.html', context)