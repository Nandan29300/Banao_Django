from django.contrib import admin
from .models import CustomUser, BlogPost

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_draft')
    list_filter = ('category', 'is_draft')
    search_fields = ('title', 'summary', 'content')
