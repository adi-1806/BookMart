from django.urls import path
from . import views

urlpatterns=[
    path("Signup", views.SignUp.as_view(), name="signup"),
    path("Home", views.ProjectHome.as_view(), name="home"),
    path("logout/",views.logoutUser, name="logout"),
    path("Bookupload/",views.BookUpload.as_view(), name="bookupload"),


    path("UserLogin", views.UserLogin.as_view(), name="userlogin"),
    path("UserHome", views.UserHome.as_view(), name="userhome"),

    path("LibraryLogin", views.LibraryLogin.as_view(), name="librarylogin"),
    path("LibraryHome", views.LibraryHome.as_view(), name="libraryhome"),

    path("BookstoreLogin", views.BookstoreLogin.as_view(), name="bookstorelogin"),
    path("BookstoreHome", views.BookstoreHome.as_view(), name="bookstorehome"),

]
