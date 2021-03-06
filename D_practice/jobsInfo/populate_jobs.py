import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobsInfo.settings')
import django
django.setup()

from jobapp.models import *
from faker import Faker
from random import *
fake = Faker()
def mobilenogen():
    d1 = randint(7,9)
    num = ''+str(d1)
    for i in range(9):
        num = num+str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager', 'Team Leader', 'Software Engineer'))
        feligibility = fake.random_element(elements=('B.Tech', 'MCA', 'PHD', 'M.Tech'))
        faddress = fake.address()
        femail = fake.email()
        fmobileno = mobilenogen()
        HyderabadJobs_record = HyderabadJobs.objects.get_or_create(date=fdate, company=fcompany,title=ftitle, eligibility=feligibility, address=faddress,email=femail, mobile_no=fmobileno)
        ChennaiJobs_record = ChennaiJobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle,
                                                                   eligibility=feligibility, address=faddress,
                                                                   email=femail, mobile_no=fmobileno)
        PuneJobs_record = PuneJobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle,
                                                                   eligibility=feligibility, address=faddress,
                                                                   email=femail, mobile_no=fmobileno)
populate(25)