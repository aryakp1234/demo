from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('ind',views.home, name='home'),
    path('home',views.about, name='about'),
]