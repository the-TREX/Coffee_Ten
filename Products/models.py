from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html
from django.utils.text import slugify

import Account.models


class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دسته بندی")
    image = models.ImageField(upload_to='images/category/', verbose_name="تصویر")
    slug = models.SlugField(unique=True, verbose_name="اسلاگ", null=True, blank=True)

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='products',
                                 verbose_name="نام دسته بندی")
    name = models.CharField(max_length=100, verbose_name="نام محصول")
    image = models.ImageField(upload_to='images/bestsellers/', verbose_name="تصویر محصول")
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True, verbose_name="اسلاگ")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="قیمت اصلی")
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                         verbose_name="قیمت تخفیف")
    discount_percent = models.PositiveSmallIntegerField(default=0, null=True, blank=True, verbose_name="درصد تخفیف")
    rating = models.PositiveSmallIntegerField(default=0, verbose_name="امتیاز کاربر")
    created_at = models.DateTimeField(auto_now=False, null=False, blank=False,
                                      verbose_name="تاریخ ثبت محصول")  # we are use it for new products
    is_bestseller = models.BooleanField(default=False, verbose_name="پرفروش")
    is_offer = models.BooleanField(default=False, verbose_name="دارای تخفیف")  # barasi offer bodan prosuct
    offer_expiration = models.DateTimeField(null=True, blank=True, verbose_name="تاریخ اتمام تخفیف")  # end time of
    breed = models.CharField(max_length=50, null=True, blank=True, verbose_name="نوع قهوه")
    caffeine_value = models.CharField(max_length=50, null=True, blank=True, verbose_name="میزان کافئن")
    birthplace = models.CharField(max_length=50, null=True, blank=True, verbose_name="خاستگاه")
    make_with = models.CharField(max_length=50, null=True, blank=True, verbose_name="مواد تشکیل‌دهنده")
    description = models.TextField(null=True, blank=True, verbose_name="توضیحات محصول")

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="100" height="100"/>')
        return format_html('<h3 style="color : red ;">تصویر ندارد</h3>')

    def save(self, *args, **kwargs):
        if not self.slug:  # barasi khali bodan slug
            base_slug = slugify(self.name)  # ye function ke slug ro standard mikone --> coffee-ten
            slug = base_slug
            counter = 1
            while Products.objects.filter(slug=slug).exists():  # agar slug tekrari bud, adad ezafe mikonim
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"


class Comment(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Account.models.User, on_delete=models.CASCADE, related_name='comments')
    title = models.CharField(max_length=100)
    suggested = models.BooleanField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=False, null=False, blank=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "نظر"
        verbose_name_plural = "نظر ها"

    def __str__(self):
        return self.title
