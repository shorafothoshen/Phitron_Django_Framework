from django.shortcuts import render

# Create your views here.
def food(request):
    return render(request,"food/index.html")

def buy(request):
    return render(request,"buy.html")