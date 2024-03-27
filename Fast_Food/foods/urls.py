
from django.urls import path
from . import views

urlpatterns = [
    path("",views.food,name='foods'),
    path("buy/",views.buy,name='buys'),
]
