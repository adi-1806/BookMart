from django.contrib import admin

# Register your models here.
from .models import Library, LibraryProfile, Bookstore, BookstoreProfile, User, Customer, CustomerProfile

admin.site.register(Bookstore)
admin.site.register(BookstoreProfile)
admin.site.register(Library)
admin.site.register(LibraryProfile)
admin.site.register(User)
admin.site.register(CustomerProfile)
admin.site.register(Customer)