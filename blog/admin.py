from django.contrib import admin
from blog.models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', "preview", "created_at", "is_published", "views_count")
    list_filter = ('title', "created_at", )