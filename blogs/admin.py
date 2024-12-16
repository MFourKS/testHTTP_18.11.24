from django.contrib import admin
from .models import Blog, Post, Tag, Comment

admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)