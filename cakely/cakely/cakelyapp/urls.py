from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.about,name='about'),
    # path('abt/',views.contact,name='contact'),

]