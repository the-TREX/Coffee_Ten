from django.db import models
from Account.models import User
from Products.models import Products


# etelaat koli az sefaresh User
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='کاربر')
    address = models.CharField(max_length=400, verbose_name='ادرس')
    email = models.EmailField(blank=True, null=True, verbose_name='ایمیل')
    phone_number = models.CharField(blank=True, null=True, max_length=12, verbose_name='شماره همراه')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ سفارش')
    is_paid = models.BooleanField(default=False, verbose_name='وضعیت پرداخت')

    def __str__(self):
        return self.user.phone

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارشات"


# mahsolati ke sefaresh dade
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items", verbose_name='')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="items")
    quantity = models.SmallIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.product.name
