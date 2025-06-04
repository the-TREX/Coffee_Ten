# from time import timezone

from django.db import models
from django.utils.text import slugify


# from Products.views import bestsellers


class Categories(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/category/')
    slug = models.SlugField(unique=True, verbose_name="اسلاگ", null=True, blank=True)

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def str(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/bestsellers/')
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_percent = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    rating = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now=False, null=False, blank=False)  # we are use it for new products
    is_bestseller = models.BooleanField(default=False)
    is_offer = models.BooleanField(default=False)  # barasi offer bodan prosuct
    offer_expiration = models.DateTimeField(null=True, blank=True)  # end time of
    breed = models.CharField(max_length=50, null=True, blank=True)
    caffeine_value = models.CharField(max_length=50, null=True, blank=True)
    birthplace = models.CharField(max_length=50, null=True, blank=True)
    make_with = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

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
