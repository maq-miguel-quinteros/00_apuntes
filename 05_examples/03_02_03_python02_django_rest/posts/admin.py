from django.contrib import admin

from posts.models import Post

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at']
