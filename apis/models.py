from django.db import models

# Create your models here.
class Register(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
