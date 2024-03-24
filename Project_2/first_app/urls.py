from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("course/",views.course),
    path("enroll/",views.enroll),
]