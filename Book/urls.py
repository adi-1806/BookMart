from django.urls import path
from . import views


urlpatterns=[
    path("Signup", views.SignUp, name="signup"),
    path("", views.ProjectHome, name="home"),
    path("logout",views.logoutUser, name="logout"),
    path("Bookupload/",views.BookUpload, name="bookupload"),
    path("Booksuploaded",views.BooksUploaded, name="booksuploaded"),


    path("Userlogin", views.UserLogin, name="userlogin"),
    path("Userhome", views.UserHome, name="userhome"),
    path("Usersellingpage", views.UserSelling, name="userselling"),
    path("Userprofile", views.UserProfile, name="userprofile"),

    path("Librarylogin", views.LibraryLogin, name="librarylogin"),
    path("Libraryhome", views.LibraryHome, name="libraryhome"),
    path("Libraryprofile", views.Libraryprofile, name="libraryprofile"),

    path("BookstoreLogin", views.BookstoreLogin, name="bookstorelogin"),
    path("BookstoreHome", views.BookstoreHome, name="bookstorehome"),
    path("Bookstoreprofile", views.Bookstoreprofile, name="bookstoreprofile"),

]