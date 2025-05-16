from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/slider/')
    is_active = models.BooleanField(default=True)

