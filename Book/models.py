from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        CUSTOMER = "CUSTOMER", "Customer"
        LIBRARY = "LIBRARY", "Library"
        BOOKSTORE = "BOOKSTORE", "Bookstore"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class LibraryManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.LIBRARY)


class Library(User):

    base_role = User.Role.LIBRARY

    Library = LibraryManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Libraries"


@receiver(post_save, sender=Library)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "LIBRARY":
        LibraryProfile.objects.create(user=instance)


class LibraryProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, null=True)
    LibraryName=models.CharField(max_length=100, null=True)
    LibraryAddress = models.CharField(max_length=200, null=True)
    LibrarianName = models.CharField(max_length=100, null=True)
    LibrarianpNo = models.IntegerField( null=True)

class BookstoreManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.BOOKSTORE)


class Bookstore(User):

    base_role = User.Role.BOOKSTORE

    Bookstore = BookstoreManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Bookstore"


class BookstoreProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, null=True)
    BookStoreName=models.CharField(max_length=100, null=True)
    BookStoreAddress = models.CharField(max_length=200, null=True)
    OwnerName = models.CharField(max_length=100, null=True)
    OwnerpNo = models.IntegerField( null=True)


@receiver(post_save, sender=Bookstore)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "BOOKSTORE":
        BookstoreProfile.objects.create(user=instance)


class CustomerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CUSTOMER)


class Customer(User):

    base_role = User.Role.CUSTOMER

    Customer = CustomerManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Customer"


class CustomerProfile(models.Model):
    Name=models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    Address = models.CharField(max_length=200, null=True)
    PhoneNo = models.IntegerField( null=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)


@receiver(post_save, sender=Customer)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CUSTOMER":
        CustomerProfile.objects.create(user=instance)