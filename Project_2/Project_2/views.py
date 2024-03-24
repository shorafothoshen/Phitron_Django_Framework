from django.http import HttpResponse
from django.shortcuts import render

def contact(request):
    return HttpResponse("this is my contact page")

def Home(request):
    return render(request,'index.html')