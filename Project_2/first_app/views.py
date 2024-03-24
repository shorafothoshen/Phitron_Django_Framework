from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"first_app/Home.html")

def course(request):
    return HttpResponse("This is my first app")

def enroll(request):
    return HttpResponse("Enroll naw in this course")
