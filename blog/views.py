from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404
# Create your views here.

# this is home page
def home_page(request):
    return render(request, 'home.html')
