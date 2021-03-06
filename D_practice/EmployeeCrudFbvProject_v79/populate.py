import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','EmployeeCrudFbvProject_v79.settings')
import django
django.setup()

from e_app.models import *
from faker import Faker
from random import *
fake = Faker()
#def mobilenogen():
#    d1 = randint(7,9)
 #   num = ''+str(d1)
  #  for i in range(9):
   #     num = num+str(randint(0,9))
    #return int(num)
def populate(n):
    for i in range(n):
        feno = randint(1001,9999)
        fname = fake.name()
        fesalary = randint(10000,100000)
        faddress = fake.city()
        emp_record = Employee.objects.get_or_create(eno=feno, ename=fname, esalary=fesalary,eaddress=faddress)
populate(20)