from django.urls import path
from . import views

urlpatterns=[
    path("Signup", views.SignUp, name="signup"),
    path("Home", views.ProjectHome, name="home"),
    path("logout/",views.logoutUser, name="logout"),
    path("Bookupload/",views.BookUpload, name="bookupload"),


    path("UserLogin", views.UserLogin, name="userlogin"),
    path("UserHome", views.UserHome, name="userhome"),

    path("LibraryLogin", views.LibraryLogin, name="librarylogin"),
    path("LibraryHome", views.LibraryHome, name="libraryhome"),

    path("BookstoreLogin", views.BookstoreLogin, name="bookstorelogin"),
    path("BookstoreHome", views.BookstoreHome, name="bookstorehome"),

]
