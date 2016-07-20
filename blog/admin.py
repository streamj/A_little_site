from django.contrib import admin
from django.contrib.auth.models import User
from blog.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    exclude = ('author',)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(Post, PostAdmin)
