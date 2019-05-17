from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main_page-home'),
    path('lost/', views.lost, name='main_page-lost'),
    path('home2/', views.home2, name='main_page-home2'),
]
