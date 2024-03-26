from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Image(request):

    data=[{"Id":1,"name":"Shorafot Hoshen","dept":"Cse"},
          {"Id":2,"name":"Farhan","dept":"Cse"},
          {"Id":3,"name":"Jishan","dept":"Cse"},
          {"Id":4,"name":"Al-amin","dept":"EEE"},
          {"Id":5,"name":"Rakib","dept":"BBA"}]
    return render(request,"first_app/Home.html",{"data":data})

# def About(request,id):
#     return render(request,"first_app/Home.html",{"id":id})
def About(request):
    print(request.GET)
    return render(request,"first_app/Home.html",{"id":request.GET})