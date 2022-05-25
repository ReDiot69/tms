from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils.translation import gettext_lazy as _


class Vendor(models.Model):
    vendor = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    phone = models.IntegerField(null=True)
    logo = models.ImageField(null=True)

    def __str__(self):
        return self.vendor


class Role(models.Model):
    role = models.CharField(max_length=25)

    def __str__(self):
        return self.role


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        # email = self.email
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(_('email'), unique=True, null=False)
    name = models.CharField(null=False, blank=False, max_length=25)
    password = models.CharField(null=False, max_length=256)
    address = models.CharField(max_length=25, null=True)
    number = models.IntegerField(null=False)
    image = models.ImageField(max_length=255, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['name', 'password', 'number']
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return str(self.name)