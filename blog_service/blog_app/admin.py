from django.contrib import admin
from .models import Blog, Post, Tag, Comment

admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets

admin.site.register(User, CustomUserAdmin)