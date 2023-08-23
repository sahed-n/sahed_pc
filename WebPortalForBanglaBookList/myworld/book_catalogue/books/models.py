from django.db import models

# Create your models here.
class Books(models.Model):
    bookName = models.CharField(max_length=255)
    authName = models.CharField(max_length=255)
    publisherName = models.CharField(max_length=255,default='Yet to know.')
    genreOfBook = models.CharField(max_length=255,default='Yet to know.')
    priceofBook = models.FloatField(default=0.0)
    ratingOfBook = models.FloatField(default=0.0)
    releaseDate = models.DateField(null=True)
    aboutOfBook = models.CharField(max_length=2128,default='Yet to know.')



