from turtle import home
from django.urls import path
from . import views
#path("", homePageView, name="home")
urlpatterns = [
        path("<int:id>", views.index, name="index"),
]