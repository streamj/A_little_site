from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

# Create your views here.

# this is home page
def home_page(request):
    return render(request, 'home.html')


def blog_home(request):
    post_list = Article.objects.all()
    return render(request, 'blog/blog_home.html', {'post_list': post_list})
