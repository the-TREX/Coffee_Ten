from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
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
    def create_user(self, username, email, phone, first_name, last_name, real_address, post_code, password=None):
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
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            phone=phone,
        )
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address", max_length=255)
    phone = models.CharField(verbose_name="تلفن همراه", max_length=11, unique=True)
    username = models.CharField(max_length=30, verbose_name="نام کاربری")
    first_name = models.CharField(max_length=80, verbose_name="نام", default="کاربر")
    last_name = models.CharField(max_length=80, verbose_name="نام خانوادگی", default="سیستم")
    real_address = models.CharField(max_length=400, verbose_name="آدرس", default="نامشخص")
    post_code = models.CharField(max_length=10, verbose_name="کد پستی", default="0000000000")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email', 'username']

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
