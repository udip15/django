
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index),
    path('test', views.test),
    path('about', views.about),
    path('page', views.page),
]