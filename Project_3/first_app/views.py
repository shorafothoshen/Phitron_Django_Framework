from django.shortcuts import render
from datetime import datetime

# Create your views here.
def Home(request):
    d={"Name":"Shorafot Hoshen","age":4 ,"birthday":datetime.now(), "lst":["python","is","best","Programming","Language"],"courses":[
        {
            "id":1,
            "Name":"Phitron",
            "fee":2000
        },
        {
            "id":2,
            "Name":"Django",
            "fee":4000
        },
        {
            "id":3,
            "Name":"DSA",
            "fee":1000
        }
    ]}
    # ami chaile peramiter hishabe render(request,"first_app/home.html",d) sudhu emn korew dite partam
    return render(request,"first_app/home.html",context=d) # context kore niya jawa hyce