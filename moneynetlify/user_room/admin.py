from django.contrib import admin
from .models import Post

# добавления поста через админ панель
@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'author', 'time_create')
