from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    business = models.CharField(max_length=255)
    message = models.TextField(max_length=2000)

    def __str__(self):
        return self.name