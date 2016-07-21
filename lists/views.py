from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from lists.models import Item, List
from lists.forms import ItemForm, ExistingListItemForm, RegisterForm
from django.http import HttpResponseRedirect

# Create your views here.
def register(request, template='lists/register.html'):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            return HttpResponseRedirect('/success/')
    else:
        form = RegisterForm()
    form = RegisterForm()
    return render(request, template, {'form': form})

def list_home(request):
    return render(request, 'lists/list_home.html', {'form': ItemForm()})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'lists/list.html', {
        'list': list_, 'form': form})

def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'lists/list_home.html', {"form": form})
