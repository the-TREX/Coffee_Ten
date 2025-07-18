# Generated by Django 5.1.5 on 2025-06-22 11:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0018_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'نظر', 'verbose_name_plural': 'نظر ها'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['-created_at'], 'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات'},
        ),
        migrations.AlterField(
            model_name='categories',
            name='image',
            field=models.ImageField(upload_to='images/category/', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=100, verbose_name='نام دسته بندی'),
        ),
        migrations.AlterField(
            model_name='products',
            name='birthplace',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='خاستگاه'),
        ),
        migrations.AlterField(
            model_name='products',
            name='breed',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='نوع قهوه'),
        ),
        migrations.AlterField(
            model_name='products',
            name='caffeine_value',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='میزان کافئن'),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Products.categories', verbose_name='نام دسته بندی'),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(verbose_name='تاریخ ثبت محصول'),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات محصول'),
        ),
        migrations.AlterField(
            model_name='products',
            name='discount_percent',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='درصد تخفیف'),
        ),
        migrations.AlterField(
            model_name='products',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='قیمت تخفیف'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='images/bestsellers/', verbose_name='تصویر محصول'),
        ),
        migrations.AlterField(
            model_name='products',
            name='is_bestseller',
            field=models.BooleanField(default=False, verbose_name='پرفروش'),
        ),
        migrations.AlterField(
            model_name='products',
            name='is_offer',
            field=models.BooleanField(default=False, verbose_name='دارای تخفیف'),
        ),
        migrations.AlterField(
            model_name='products',
            name='make_with',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='مواد تشکیل\u200cدهنده'),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=100, verbose_name='نام محصول'),
        ),
        migrations.AlterField(
            model_name='products',
            name='offer_expiration',
            field=models.DateTimeField(blank=True, null=True, verbose_name='تاریخ اتمام تخفیف'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='قیمت اصلی'),
        ),
        migrations.AlterField(
            model_name='products',
            name='rating',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='امتیاز کاربر'),
        ),
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True, verbose_name='اسلاگ'),
        ),
    ]
