from django.db import models

# Create your models here.
#Abstract Base Class Model
class ContactInfo(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    address = models.CharField(max_length=264)
    class Meta:
        abstract = True
class Student(ContactInfo):
    rollno = models.IntegerField()
    marks = models.IntegerField()
class Teacher(ContactInfo):
    subject = models.CharField(max_length=64)
    salary = models.FloatField()


#Multi Table Inheritance

class ContactInfo1(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    address = models.CharField(max_length=264)

class Student1(ContactInfo1):
    rollno = models.IntegerField()
    marks = models.IntegerField()

class Teacher1(ContactInfo1):
    subject = models.CharField(max_length=64)
    salary = models.FloatField()

#Multi-Level Inheritance
class Parent(models.Model):
    fd1 = models.CharField(max_length=64)
    fd2 = models.CharField(max_length=64)
class Child(Parent):
    fd3 = models.CharField(max_length=64)
    fd4 = models.CharField(max_length=64)
class Subchild(Child):
    fd5 = models.CharField(max_length=64)