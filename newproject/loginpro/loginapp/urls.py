from django.urls import path
from .import views

urlpatterns = [
    path('',views.base,name='home' ),
    path('login/',views.user_login,name='loginn'),
    path('signup/',views.user_signup,name='signup'),
    path('logout/',views.user_logout,name='logout1'),
]
