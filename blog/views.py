from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'home.html')

def blog_home(request):
    return render(request, 'blog/blog_home.html')
