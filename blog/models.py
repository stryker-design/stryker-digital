from django.db import models
from django.urls import reverse
from tinymce import models as tinymce_models


# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='Andy Walker')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True) 
    image =  models.ImageField(upload_to='images/', default='images/default.png')
    description = models.CharField(max_length=255)
    body = tinymce_models.HTMLField(blank=False, null=True)
    time_to_read = models.CharField(max_length=10, default='5')

    def __str__(self):
        return self.title
    