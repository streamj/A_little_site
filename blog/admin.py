from django.contrib import admin
from blog.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_dispaly = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    raw_id_fields = ('author',)
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy='publish'
    orderng = ['status', 'publish']

admin.site.register(Post, PostAdmin)
