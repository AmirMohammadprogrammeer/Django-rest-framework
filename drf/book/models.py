from django.db import models

# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=100)
    book_name = models.CharField(max_length=100)
    code = models.IntegerField()

    def __str__(self):
        return self.book_name

class Writer(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    book = models.ManyToManyField(Book,related_name="writers")

    def __str__(self):
        return self.first_name +" "+self.last_name