import os
from django.http import HttpResponse, HttpResponseRedirect
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
        if('uname' in request.session): 
            del request.session['uname']  
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
        # username=''
        
        # if('uname' in request.session):
        #     username=request.session['uname'] 
        current_user = request.user
        
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
                image = image,
                book_owner = current_user
            )
            details.save()

            return render(request, "Book/Userselling.html")
        
        elif ownertype=="Bookstore":
            details = Books_Store(
                name = bookname,
                author = author,
                publications= publications,
                edition = edition,
                price = price,
                quantity = quantity,
                purpose = purpose,
                image = image,
                book_owner = current_user
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
                book_owner = current_user
            )
            details.save()
            return render(request,'Book/LibraryHome.html')

    return render(request, "Book/BookUpload.html")
        
@login_required(login_url='home')
def BooksUploaded(request):
    # username=''
    # if('uname' in request.session):
    #         username=request.session['uname']
    current_user = request.user
            
    details= User.objects.get(username=current_user)

    if details.role == "LIBRARY":
        books_sale= Books_Library.objects.filter(book_owner=current_user, purpose ='Sale')
        books_rent= Books_Library.objects.filter(book_owner=current_user, purpose ='Rent')

        return render(request, "Book/Uploadedbooks.html",{
             "books_sale" : books_sale,
             "books_rent" : books_rent
        })
    
    if details.role == "BOOKSTORE":
        books_sale= Books_Store.objects.filter(book_owner=current_user, purpose ='Sale')
        books_rent= Books_Store.objects.filter(book_owner=current_user, purpose ='Rent')

        return render(request, "Book/Uploadedbooks.html",{
             "books_sale" : books_sale,
             "books_rent" : books_rent
        })
    
    
    if details.role == "CUSTOMER":
        books_sale= Books_User.objects.filter(book_owner=current_user, purpose ='Sale')
        books_rent= Books_User.objects.filter(book_owner=current_user, purpose ='Rent')

        return render(request, "Book/Uploadedbooks.html",{
             "books_sale" : books_sale,
             "books_rent" : books_rent
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
    return render(request, "Book/Userhome.html")

@login_required(login_url='home')
def UserSelling(request):
    return render(request, "Book/Userselling.html")

@login_required(login_url='home')
def UserProfile(request):
    current_user=request.user

    details = CustomerProfile.objects.get(user=current_user)
    
    if request.method == "POST":
        
        name = request.POST['name']
        address = request.POST['address']
        email= request.POST['Email']
        pno = request.POST['Pno']
        imagefield = request.FILES["image"]

        if imagefield!="":
            if details.image!="":
                os.remove(details.image.path)

            details.image = imagefield
            details.save()
        
        if name!="":
            CustomerProfile.objects.filter(user=details.user).update(Name=name)

        if email!="":
            CustomerProfile.objects.filter(user=details.user).update(email=email)

        if address!="":
            CustomerProfile.objects.filter(user=details.user).update(Address=address)

        if pno!="":
            CustomerProfile.objects.filter(user=details.user).update(PhoneNo=pno)
       
        return HttpResponseRedirect("/Userhome")
    
    return render(request, "Book/Userprofile.html",{
                    "details" : details
                  })
    
def UserPurBookstore(request):
    books = BookstoreProfile.objects.filter()
    return render(request, "Book/UserPurBstore.html",{
        "books" : books
    })

def UserPurUser(request):
    books = Books_User.objects.filter(purpose='Sale')
    return render(request, "Book/UserPurUser.html",{
        "books" : books
    })

def UserRentLib(request):
    books = LibraryProfile.objects.filter()
    details = LibraryProfile.objects.get(LibraryName='warangal')
    return render(request, "Book/UserRentLib.html",{
        "books" : books
    })
    
def UserRentUser(request):
    books = Books_User.objects.filter(purpose='Rent')
    return render(request, "Book/UserRentUser.html",{
        "books" : books
    })

def IndiLibraryBooks(request, pk):
    details = LibraryProfile.objects.get(id=pk)
    books= Books_Library.objects.filter(book_owner =details.user)
    if books:
        return render(request, "Book/UserLibBooks.html",{
            "books" : books
        })
    else:
        return HttpResponse('NO books present')
    
def IndiBookstoreBooks(request, pk):
    details = BookstoreProfile.objects.get(id=pk)
    books= Books_Store.objects.filter(book_owner =details.user)
    if books:
        return render(request, "Book/UserBSBooks.html",{
            "books" : books
        })
    else:
        return HttpResponse('NO books present')

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
      
@login_required(login_url='home')
def Bookstoreprofile(request):
    current_user = request.user
    details = BookstoreProfile.objects.get(user=current_user)
    
    if request.method == "POST":
        
        BookStoreName = request.POST['BookStoreName']
        BookStoreAddress = request.POST['BookStoreAddress']
        OwnerName = request.POST['OwnerName']
        email= request.POST['Email']
        OwnerpNo = request.POST['OwnerpNo']
        imagefield = request.FILES["image"]

        if imagefield!="":
            if details.image!="":
                os.remove(details.image.path)

            details.image = imagefield
            details.save()

        
        if BookStoreName!="":
            BookstoreProfile.objects.filter(user=details.user).update(BookStoreName=BookStoreName)

        if email!="":
            BookstoreProfile.objects.filter(user=details.user).update(email=email)

        if BookStoreAddress!="":
            BookstoreProfile.objects.filter(user=details.user).update(BookStoreAddress=BookStoreAddress)

        if OwnerpNo!="":
            BookstoreProfile.objects.filter(user=details.user).update(OwnerpNo=OwnerpNo)
        
        if OwnerName!="":
            BookstoreProfile.objects.filter(user=details.user).update(OwnerName=OwnerName)

        return HttpResponseRedirect("/Bookstorehome")
    
    return render(request, "Book/Bookstoreprofile.html",{
                    "details" : details
                  })
            
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
        
@login_required(login_url='home')
def Libraryprofile(request):
    current_user = request.user
    details = LibraryProfile.objects.get(user=current_user)
    
    if request.method == "POST":
        
        LibraryName = request.POST['LibraryName']
        LibraryAddress = request.POST['LibraryAddress']
        LibrarianName = request.POST['LibrarianName']
        email= request.POST['Email']
        LibrarianpNo = request.POST['LibrarianpNo']
        imagefield = request.FILES["image"]
        print(imagefield)

        if imagefield!="":
            print(imagefield)
            if details.image!="":
                os.remove(details.image.path)

            details.image = imagefield
            details.save()
        
        if LibraryName!="":
            LibraryProfile.objects.filter(user=details.user).update(LibraryName=LibraryName)

        if email!="":
            LibraryProfile.objects.filter(user=details.user).update(email=email)

        if LibraryAddress!="":
            LibraryProfile.objects.filter(user=details.user).update(LibraryAddress=LibraryAddress)

        if LibrarianpNo!="":
            LibraryProfile.objects.filter(user=details.user).update(LibrarianpNo=LibrarianpNo)
        
        if LibrarianName!="":
            LibraryProfile.objects.filter(user=details.user).update(LibrarianName=LibrarianName)

        return HttpResponseRedirect("/Libraryhome")
    
    return render(request, "Book/Libraryprofile.html",{
                    "details" : details
                  })