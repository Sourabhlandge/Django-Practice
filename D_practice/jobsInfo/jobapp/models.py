from django.db import models

# Create your models here.
class HyderabadJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_no = models.IntegerField()

class ChennaiJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_no = models.IntegerField()

class PuneJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_no = models.IntegerField()
