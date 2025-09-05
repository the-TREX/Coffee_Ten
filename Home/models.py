from django.db import models
from Products.models import Categories
class Slider(models.Model):
    category = models.ForeignKey(Categories , on_delete=models.CASCADE , related_name='slider_category' , null=True , blank=True , default=None)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/slider/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "اسلاید"
        verbose_name_plural = "اسلایدر"
