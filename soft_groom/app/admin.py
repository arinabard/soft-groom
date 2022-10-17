from django.contrib import admin
from .models import Author, Comment, Contact

# Register your models here.

admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Contact)