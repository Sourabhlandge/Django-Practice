from django.db import models

# Create your models here.
class FilterModel(models.Model):
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    date = models.DateField()
