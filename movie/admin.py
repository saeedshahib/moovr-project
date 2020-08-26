from django.contrib import admin
from .models import Movie
from .models import Comment
# Register your models here.

admin.site.register(Movie)
admin.site.register(Comment)