from django.urls import path
from . import views

urlpatterns=[
    path("Signup", views.SignUp.as_view(), name="signup"),
    path("logout/",views.logoutUser, name="logout"),
    path("Login", views.Login.as_view(), name="login"),
    path("Home", views.Home.as_view(), name="home"),
]
