from django.contrib import admin

# Register your models here.
from .models import Books_Library, Books_Store, Books_User, Library, LibraryProfile, Bookstore, BookstoreProfile, User, Customer, CustomerProfile

admin.site.register(Bookstore)
admin.site.register(BookstoreProfile)
admin.site.register(Library)
admin.site.register(LibraryProfile)
admin.site.register(User)
admin.site.register(CustomerProfile)
admin.site.register(Customer)
admin.site.register(Books_User)
admin.site.register(Books_Library)
admin.site.register(Books_Store)
