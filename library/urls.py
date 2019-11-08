from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('rules/', views.rules, name='rules'),
    path('form/', views.form, name='form'),
  
    

]