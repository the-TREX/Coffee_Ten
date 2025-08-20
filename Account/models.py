from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
<<<<<<< HEAD
=======
from django.contrib.auth.models import PermissionsMixin
>>>>>>> c733fe4115b9e3fff773082e92d5ab50f83a3dab
from django.db import models


class Contact(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "ارتباط باما"
        verbose_name_plural = "ارتباط باما"


class UserManager(BaseUserManager):
<<<<<<< HEAD
    def create_user(self, username, email, phone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
=======
    def create_user(self, username, email, phone, first_name, last_name, real_address, post_code, password=None):
>>>>>>> c733fe4115b9e3fff773082e92d5ab50f83a3dab
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            real_address=real_address,
            post_code=post_code,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone, password=None):
<<<<<<< HEAD
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
            phone=phone,
        )
=======
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            phone=phone,
        )
        user.set_password(password)
>>>>>>> c733fe4115b9e3fff773082e92d5ab50f83a3dab
        user.is_admin = True
        user.save(using=self._db)
        return user


<<<<<<< HEAD
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=30, verbose_name="نام کاربری")
    phone = models.CharField(max_length=15, unique=True, verbose_name="تلفن همراه")
=======
<<<<<<< HEAD
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, verbose_name="ایمیل", unique=True)
=======
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address", max_length=255)
>>>>>>> d5b69549689337c2da335bf34d0b440626b39ab0
    phone = models.CharField(verbose_name="تلفن همراه", max_length=11, unique=True)
    username = models.CharField(max_length=30, verbose_name="نام کاربری")
    first_name = models.CharField(max_length=80, verbose_name="نام", default="کاربر")
    last_name = models.CharField(max_length=80, verbose_name="نام خانوادگی", default="سیستم")
    real_address = models.CharField(max_length=400, verbose_name="آدرس", default="نامشخص")
    post_code = models.CharField(max_length=10, verbose_name="کد پستی", default="0000000000")
>>>>>>> c733fe4115b9e3fff773082e92d5ab50f83a3dab
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

<<<<<<< HEAD
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []
=======
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email', 'username']
>>>>>>> c733fe4115b9e3fff773082e92d5ab50f83a3dab

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"
