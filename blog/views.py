from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from datetime import datetime
from django.http import Http404
# Create your views here.

# this is home page
def home_page(request):
    return render(request, 'home.html')


def blog_home(request):
    post_list = Article.objects.all()
    return render(request, 'blog/blog_home.html', {'post_list': post_list})

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'blog/post.html', {'post': post})
