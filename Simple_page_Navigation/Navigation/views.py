from django.shortcuts import render

# Create your views here.

def About(request):
    return render(request,"navigation/about.html")

def Contact(request):
    return render(request,"navigation/contact.html")