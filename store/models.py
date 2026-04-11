from django.db import models


class posts(models.Model):
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=20)
    image=models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

# Create your models here.
