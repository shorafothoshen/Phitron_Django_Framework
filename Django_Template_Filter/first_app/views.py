from django.shortcuts import render
from datetime import datetime

# Create your views here.

def Filter(request):
    dic={"name":"Shorafot Hoshen","age":20,"lst":["Python","is","the","best","Programmig","Language"],"Today":datetime.now(),"val":"","addValue":30,"addlst":["1","2","3"],"cap":"earthly","cutFilter1":"String with spaces","cutFilter2":"January - February - March", "Distsort":[
   {'name': 'Abhi', 'age': 29},
   {'name': 'Sonia', 'age': 25},
   {'name': 'Rahul', 'age': 36},
],"Escape":"<p>You are <em>pretty</em> smart!</p>","FirstFilter":['Apple', 'Mango', 'Orange'],"LastFilter":['Apple', 'Mango', 'Orange'],"LineNum":"cat dog horse","TitleFilter":"Django rest framework","RandomFilter":['Banana', 'Mango', 'Orange'],"SliceFilter":['Banana', 'Mango', 'Orange'],"TimeFilter":datetime.now(),"TimesinceFilter":datetime.now()}
    return render(request,"first_app/Filter.html",context=dic)
