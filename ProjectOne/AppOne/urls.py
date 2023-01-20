from django.urls import path
from . import views

urlpatterns = [
    path("New/", views.appone, name="new"),
    path("AppOne/", views.index, name='index')
]
