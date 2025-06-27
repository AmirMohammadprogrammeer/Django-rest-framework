from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    owner = models.ForeignKey(User,related_name='books',null=True,blank=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name