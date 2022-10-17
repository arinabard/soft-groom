from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(blank=False, max_length=100)
    email = models.EmailField(blank=False, primary_key=True)

class Comment(models.Model):

    content = models.TextField(blank=False)
    issued = models.DateTimeField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE, default='')
    
class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=13, blank=False)