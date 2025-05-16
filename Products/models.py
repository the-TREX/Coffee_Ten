# from time import timezone

from django.db import models
from django.utils.text import slugify

# from Products.views import bestsellers


class Categories(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/category/')
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Categories, self).save(*args, **kwargs)


class Products(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/bestsellers/')
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2 , null=True ,blank=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2 , null=True, blank=True)
    discount_percent = models.PositiveSmallIntegerField(default=0 , null=True, blank=True)
    rating = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now=False , null=False , blank=False) # we are use it for new products
    is_bestseller = models.BooleanField(default=False)
    is_offer = models.BooleanField(default=False) # barasi offer bodan prosuct
    offer_expiration = models.DateTimeField(null=True, blank=True) # end time of

    def __str__(self):
        return self.name
