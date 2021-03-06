from django.db import models

# Create your models here.
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esalary__gte=15000)

    def get_emp_salary_range(self,esalary1,esalary2):
        return super().get_queryset().filter(esalary__range=(esalary1,esalary2)).order_by('esalary')

    def get_emp_sorted_by(self,param):
        return super().get_queryset().order_by('ename')
#################################################################
class CustomManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('ename')
class CustomManager3(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esalary__lt=15000)

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=50)
    esalary = models.FloatField()
    eaddress = models.CharField(max_length=250)
    objects = CustomManager()
class ProxyEmployee(Employee):
    objects = CustomManager2()
    class Meta:
        proxy = True
class ProxyEmployee2(Employee):
    objects = CustomManager3()
    class Meta:
        proxy = True