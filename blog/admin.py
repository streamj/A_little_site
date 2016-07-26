from django.contrib import admin
from .models import Post, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_dispaly = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    raw_id_fields = ('author',)
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy='publish'
    orderng = ['status', 'publish']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
