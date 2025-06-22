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
