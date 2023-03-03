from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Library,User, Bookstore, Books_Library, Books_Store,Books_User, Customer, CustomerProfile, LibraryProfile, BookstoreProfile
from django.contrib.auth.decorators import login_required


# Create your views here

def ProjectHome(request):
        if request.method=="POST":
            userbutton = request.POST['user']
            librarybutton = request.POST['library']
            bookstorebutton = request.POST['bookstore']


            if userbutton=='User':
                return redirect('userlogin')
            
            elif librarybutton=='Library':
                return redirect('librarylogin')
            
            elif bookstorebutton=='Bookstore':
                return redirect('bookstorelogin')

        return render(request, "Book/homepage.html")

def logoutUser(request):
        logout(request)
        return render(request, 'Book/homepage.html')

def SignUp(request):
    if request.method== "POST":    
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


    return render(request, "Book/signup.html")
    
@login_required(login_url='home')
def BookUpload(request):
    if request.method=='POST':
        username=''
        
        if('uname' in request.session):
            username=request.session['uname'] 
        
        bookname = request.POST['Bkname']
        author = request.POST['Author']
        edition = request.POST['edition']
        price = request.POST['price']
        publications = request.POST['publications']
        quantity = request.POST['quantity']
        purpose = request.POST['sale']
        image = request.FILES["image"]
        ownertype = request.POST['ownertype']


        if ownertype=="User":
            details = Books_User(
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

            return render(request, "Book/Libraryhome.html")
        
        elif ownertype=="Bookstore":
            details = Books_Store(
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

            return render(request, "Book/Bookstorehome.html")
        
        elif ownertype == "Library":
            details = Books_Library(
                name = bookname,
                author = author,
                publications= publications,
                edition = edition,
                price = price,
                quantity = quantity,
                purpose = purpose,
                image = image,
                book_owner = username
            )
            details.save()
            return render(request,'Book/LibraryHome.html')

    return render(request, "Book/BookUpload.html")
        
@login_required(login_url='home')
def BooksUploaded(request):
    username=''
    if('uname' in request.session):
            username=request.session['uname']
            
    details= User.objects.get(username=username)

    if details.role == "LIBRARY":
        books= Books_Library.objects.filter(book_owner=username)
        return render(request, "Book/Uploadedbooks.html",{
             "books" : books
        })
    
    if details.role == "BOOKSTORE":
        books= Books_Library.objects.filter(book_owner=username)
        return render(request, "Book/Uploadedbooks.html",{
             "books" : books
        })
    
    if details.role == "CUSTOMER":
        books= Books_Library.objects.filter(book_owner=username)
        return render(request, "Book/Uploadedbooks.html",{
             "books" : books
        })
    
    return render(request, "Book/Uploadedbooks.html")

#--------------------------------------------------------

def UserLogin(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['pwd']

        details = Customer.objects.get(role = 'Customer', username= username)

        if details.role == 'CUSTOMER':
            user= authenticate(request, username=username, password=password)

            if user is not None:
                request.session['uname']=username
                login(request, user)
                return redirect("userhome")
            else:
                messages.info(request, 'Username Or Password is incorrect')
                return render(request, "Book/login.html")

    return render(request, "Book/login.html")

@login_required(login_url='home')
def UserHome(request):
#     def Userhome(request):
#         if "uname" in request.session: 
    return render(request, "Book/Userhome.html")

def UserSelling(request):
    return render(request, "Book/Userselling.html")
    
#-----------------------------------

def BookstoreLogin(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['pwd']

        details = Bookstore.objects.get(role = 'Bookstore', username= username)

        if details.role == 'BOOKSTORE':
            user= authenticate(request, username=username, password=password)

            if user is not None:
                request.session['uname']=username
                login(request, user)
                return redirect("bookstorehome")
            else:
                messages.info(request, 'Username Or Password is incorrect')
                return render(request, "Book/Bookstorelogin.html")

    return render(request, "Book/Bookstorelogin.html")

@login_required(login_url='home')
def BookstoreHome(request):

    return render(request, "Book/Bookstorehome.html")
      
            
#---------------------------------------------------------------
def LibraryLogin(request):
    if request.method== "POST":
        username=request.POST['username']
        password=request.POST['pwd']

        details = Library.objects.get(role = 'Library', username= username)

        if details.role == 'LIBRARY':
            user= authenticate(request, username=username, password=password)

            if user is not None:
                request.session['uname']=username
                login(request, user)
                return redirect("libraryhome")
            else:
                messages.info(request, 'Username Or Password is incorrect')
                return render(request, "Book/Librarylogin.html")
        
    return render(request, "Book/librarylogin.html")

@login_required(login_url='home')
def LibraryHome(request):

        if request.method == "POST":
                return render(request, "Book/BookUpload.html")

        return render(request, "Book/Libraryhome.html")
        