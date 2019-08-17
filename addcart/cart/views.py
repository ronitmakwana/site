from django.shortcuts import render
from django.http import HttpResponse
from .forms import productform

def pro(request):
    return HttpResponse('<h1>Welcome to my site<h1>')

def proview(request):
     form=productform(request.POST)
     if form.is_valid():
         form.save()
     return render(request,'forms.html',{'key':form})