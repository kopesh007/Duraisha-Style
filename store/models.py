from django.db import models


class posts(models.Model):
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=20)
    image=models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
class user_data(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    interest=models.CharField(max_length=300)
    message=models.CharField( default = "nothing", max_length=500)

# Create your models here.
