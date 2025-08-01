from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):
<<<<<<< HEAD
    def create_user(self, username, email, phone, password=None):
=======
    def create_user(self, username, email, phone, first_name, last_name, real_address, post_code, password=None):
>>>>>>> Try_To_MakeBetter_Account_App
        if not email:
            raise ValueError("Email is required")
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            phone=phone,
<<<<<<< HEAD
=======
            first_name=first_name,
            last_name=last_name,
            real_address=real_address,
            post_code=post_code,

>>>>>>> Try_To_MakeBetter_Account_App
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone, password=None):
<<<<<<< HEAD
        user = self.create_user(username, email, phone, password)
=======
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            phone=phone,
        )
        user.set_password(password)
>>>>>>> Try_To_MakeBetter_Account_App
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


<<<<<<< HEAD
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, unique=True)
=======
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address", max_length=255)
    phone = models.CharField(verbose_name="تلفن همراه", max_length=11, unique=True)
    username = models.CharField(max_length=30, verbose_name="نام کاربری")
    first_name = models.CharField(max_length=80, verbose_name="نام", default="کاربر")
    last_name = models.CharField(max_length=80, verbose_name="نام خانوادگی", default="سیستم")
    real_address = models.CharField(max_length=400, verbose_name="آدرس", default="نامشخص")
    post_code = models.CharField(max_length=10, verbose_name="کد پستی", default="0000000000")
>>>>>>> Try_To_MakeBetter_Account_App
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username', 'email']

    objects = UserManager()

<<<<<<< HEAD
=======
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email', 'username']

>>>>>>> Try_To_MakeBetter_Account_App
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None): return True
    def has_module_perms(self, app_label): return True

    @property
    def is_staff(self):
        return self.is_admin


class OTP(models.Model):
    phone = models.CharField(max_length=15)
    code = models.CharField(max_length=6)
    created = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return timezone.now() - self.created < timezone.timedelta(minutes=2)

    def __str__(self):
        return f"{self.phone} - {self.code}"
