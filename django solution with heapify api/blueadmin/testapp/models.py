from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.db.models.base import Model


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, first_name=None, last_name=None, username=None,
                    password=None,
                    is_admin=False, is_staff=False, is_active=True, is_superuser=False):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.first_name = first_name
        user.last_name = last_name

        user.set_password(password)

        user.username = username
        user.admin = is_admin
        user.staff = is_staff
        user.is_superuser = is_superuser
        user.is_staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name=None, last_name=None,  username=None,
                         password=None):

        user = self.create_user(
            email,
            first_name,
            last_name,
            username=username,
            password=password,
            is_staff=True,
            is_superuser=True,
            is_admin=True,

        )
        return user


class Users(AbstractUser):

    first_name = models.CharField(
        'First Name', max_length=120, unique=False, null=True, blank=True)
    last_name = models.CharField(
        'Last Name', max_length=120, unique=False, null=True, blank=True)
    email = models.EmailField('Email', unique=True)
    username = models.CharField('Username', max_length=120, unique=True)
    password = models.CharField(
        'Password', max_length=120, unique=False, null=False)
    birth_date = models.DateField('Date of Birth', null=True, blank=True)
    updated_at = models.DateTimeField('Updated Date', auto_now=True)
    created_at = models.DateTimeField('Created Date', auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.username)

    objects = UserManager()


class UserAddress(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user)


class UserFeedback(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user)
