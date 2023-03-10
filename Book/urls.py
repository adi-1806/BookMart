from django.urls import path
from . import views


urlpatterns=[
    path("Signup", views.SignUp, name="signup"),
    path("", views.ProjectHome, name="home"),
    path("logout",views.logoutUser, name="logout"),
    path("Bookupload/",views.BookUpload, name="bookupload"),
    path("Booksuploaded",views.BooksUploaded, name="booksuploaded"),
    path("Appointment/<str:pk>/",views.AppointmentPage, name="appointment"),


    path("Userlogin", views.UserLogin, name="userlogin"),
    path("Userhome", views.UserHome, name="userhome"),
    path("Usersellingpage", views.UserSelling, name="userselling"),
    path("Userprofile", views.UserProfile, name="userprofile"),
    path("UserPurchasingBookstore", views.UserPurBookstore, name="userpurchasingbookstore"),
    path("UserPurchasingUser", views.UserPurUser, name="userpurchasingUser"),
    path("UserRentingLib", views.UserRentLib, name="userrentinglib"),
    path("UserRentingUser", views.UserRentUser, name="userrentingUser"),
    path("UserLibBooks/<str:pk>/", views.IndiLibraryBooks, name="indilibbooks"),
    path("UserBSBooks/<str:pk>/", views.IndiBookstoreBooks, name="indibsbooks"),


    path("Librarylogin", views.LibraryLogin, name="librarylogin"),
    path("Libraryhome", views.LibraryHome, name="libraryhome"),
    path("Libraryprofile", views.Libraryprofile, name="libraryprofile"),
    path("Libraryappointment/<str:pk>/",views.LibraryAppointmentPage, name="libraryappointment"),

    path("Bookstorelogin", views.BookstoreLogin, name="bookstorelogin"),
    path("Bookstorehome", views.BookstoreHome, name="bookstorehome"),
    path("Bookstoreprofile", views.Bookstoreprofile, name="bookstoreprofile"),
    path("Bookstoreappointment/<str:pk>/",views.BookstoreAppointmentPage, name="bookstoreappointment"),

]