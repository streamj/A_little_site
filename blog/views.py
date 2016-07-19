from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

# Create your views here.

# this is home page
def home_page(request):
    return render(request, 'home.html')


def blog_home(request):
    return render(request, 'blog/blog_home.html')

def detail(request, args):
    post = Article.objects.all()[int(args)]
    str = ("title = %s, category= %s, date_time=%s, content=%s" %
           (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)
