from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return HttpResponse("<p>This is Home</p>")
    #return render(request, 'home.html')
