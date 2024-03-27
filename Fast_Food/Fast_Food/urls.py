
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("foods/",include("foods.urls")),
    path("",views.Home),
    path("buy/",views.Buy,name='buy')
]
