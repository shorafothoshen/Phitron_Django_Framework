from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render(request,"index.html")

def contact(request):
    return HttpResponse("This is contact Page")