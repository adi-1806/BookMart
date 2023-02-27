from django.shortcuts import render, HttpResponseRedirect,redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Library, Bookstore, Books_Library, Customer, CustomerProfile, LibraryProfile, BookstoreProfile
from django.contrib.auth.decorators import login_required


# Create your views here


#@login_required(login_url='loginpage')
class ProjectHome(View):
    def post(self, request):
        userbutton = request.POST['user']
        librarybutton = request.POST['library']
        bookstorebutton = request.POST['bookstore']


        if userbutton=='User':
            return redirect('userlogin')
        
        elif librarybutton=='Library':
            return redirect('librarylogin')
        
        elif bookstorebutton=='Bookstore':
            return redirect('bookstorelogin')

    def get(self, request):
        return render(request, "Book/homepage.html")

def logoutUser(request):
    logout(request)
    #messages.info(request, 'Logout successful')
    return redirect('login')

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

            return render(request, "Book/homepage.html")


    def get(self, request):
        return render(request, "Book/signup.html")
    
class BookUpload(View):
    def post(self, request):
        bookname = request.POST['Bkname']
        author = request.POST['Author']
        edition = request.POST['edition']
        price = request.POST['price']
        publications = request.POST['publications']
        quantity = request.POST['quantity']
        purpose = request.POST['sale']
        ownertype = request.POST['ownertype']

        # if ownertype=="User":
        #     tablename = "Books_User"
        #     urlname = 'UserHome'
        # elif ownertype=="Bookstore":
        #     tablename = "Books_Store"
        #     urlname = 'LibraryHome'
        # elif ownertype == "Library":
        #     tablename = "Books_Library"
        #     urlname = 'BookstoreHome' {{tablename}} {{urlname}}

        details = Books_Library(
            name = bookname,
            author = author,
            publications= publications,
            edition = edition,
            price = price,
            quantity = quantity,
            purpose = purpose,
            book_owner = username
        )
        details.save()

        return redirect('LibraryHome')

    def get(self, request):
        return render(request, "Book/BookUpload.html")

#--------------------------------------------------------
username = ''
class UserLogin(View):
    def post(self, request):
        username=request.POST['username']
        password=request.POST['pwd']

        details = Customer.objects.get(role = 'Customer', username= username)

        if details.role == 'CUSTOMER':
            user= authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('userhome')
            else:
                messages.info(request, 'Username Or Password is incorrect')
                return render(request, "Book/login.html")
        
    def get(self, request):
        return render(request, "Book/login.html")

class UserHome(View):
    def post(self, request):
        pass

    def get(self, request):
        return render(request, "Book/Userhome.html")
    
#-----------------------------------

class BookstoreLogin(View):
    def post(self, request):
        username=request.POST['username']
        password=request.POST['pwd']

        details = Bookstore.objects.get(role = 'Bookstore', username= username)

        if details.role == 'BOOKSTORE':
            user= authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('bookstorehome')
            else:
                messages.info(request, 'Username Or Password is incorrect')
                return render(request, "Book/Bookstorelogin.html")
        
    def get(self, request):
        return render(request, "Book/Bookstorelogin.html")

class BookstoreHome(View):
    def post(self, request):
        pass

    def get(self, request):
        return render(request, "Book/Bookstorehome.html")
    
#---------------------------------------------------------------

class LibraryLogin(View):
    def post(self, request):
        username=request.POST['username']
        password=request.POST['pwd']

        details = Library.objects.get(role = 'Library', username= username)

        if details.role == 'LIBRARY':
            user= authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('libraryhome')
            else:
                messages.info(request, 'Username Or Password is incorrect')
                return render(request, "Book/Librarylogin.html")
        
    def get(self, request):
        return render(request, "Book/librarylogin.html")

class LibraryHome(View):
    def post(self, request):
        pass

    def get(self, request):
        return render(request, "Book/Libraryhome.html")