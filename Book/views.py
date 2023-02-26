from django.shortcuts import render, HttpResponseRedirect,redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Library, Bookstore, Customer, CustomerProfile, LibraryProfile, BookstoreProfile
from django.contrib.auth.decorators import login_required


# Create your views here.

class SignUp(View):
    def post(self, request):
        form=request.POST['Yes']
        if form=='Submit':
            username = request.POST['name']
            email = request.POST['email']
            password = request.POST['pwd']
            usertype = request.POST['user_type']
            
            if usertype == 'User' :
                Customer.objects.create_user(username = username, password = password)
                #CustomerProfile.objects.filter(user= username).update(email=email)
                

            elif usertype == 'Bookstore':
                Bookstore.objects.create_user(username = username, password = password)
                # details= BookstoreProfile(
                #     email = email
                # )
                # details.save()

            elif usertype == 'Library' :
                Library.objects.create_user(username = username, password = password)
                # details=LibraryProfile(
                #     email = email
                # )
                # details.save()

            return render(request, "Book/home.html")


    def get(self, request):
        return render(request, "Book/signup.html")

class Login(View):
    def post(self, request):
        username=request.POST['username']
        password=request.POST['pwd']

        user= authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username Or Password is incorrect')
            return render(request, "Book/login.html")
        
    def get(self, request):
        return render(request, "Book/login.html")
    
def logoutUser(request):
    logout(request)
    #messages.info(request, 'Logout successful')
    return redirect('login')

#@login_required(login_url='loginpage')
class Home(View):
    def post(self, request):
        pass

    def get(self, request):
        return render(request, "Book/home.html")
