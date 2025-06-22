from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/slider/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "اسلاید"
        verbose_name_plural = "اسلایدر"
