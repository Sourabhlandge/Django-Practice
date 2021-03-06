from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    marks = models.IntegerField()

class Employee(models.Model):
    ename = models.CharField(max_length=20)
    eno = models.IntegerField()
    esalary = models.FloatField()
    eadd = models.CharField(max_length=50)
    #def __str__(self):
     #   return self.ename,self.eno
