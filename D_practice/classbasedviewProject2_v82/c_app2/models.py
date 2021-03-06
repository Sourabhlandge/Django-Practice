from django.db import models

# Create your models here.
class BookModel(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    page = models.PositiveIntegerField()
    price = models.FloatField()
