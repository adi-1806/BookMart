from django.urls import path
from . import views

urlpatterns=[
    path("Signup", views.SignUp, name="signup"),
    path("Home", views.ProjectHome, name="home"),
    path("logout",views.logoutUser, name="logout"),
    path("Bookupload/",views.BookUpload, name="bookupload"),
    path("Booksuploaded",views.BooksUploaded, name="booksuploaded"),


    path("UserLogin", views.UserLogin, name="userlogin"),
    path("UserHome", views.UserHome, name="userhome"),
    path("Usersellingpage", views.UserSelling, name="userselling"),

    path("LibraryLogin", views.LibraryLogin, name="librarylogin"),
    path("LibraryHome", views.LibraryHome, name="libraryhome"),

    path("BookstoreLogin", views.BookstoreLogin, name="bookstorelogin"),
    path("BookstoreHome", views.BookstoreHome, name="bookstorehome"),

]
