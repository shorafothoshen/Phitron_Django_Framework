from django.urls import path
from . import views

urlpatterns = [
    path("",views.Image, name="home"),
    # path("about/<int:id>/",views.About, name="about"),
    path("about/",views.About, name="about"),
]
