from django.shortcuts import render,redirect
from o_app.models import Employee
from django.db.models import Q,Avg,Sum,Max,Min,Count
from django.db.models.functions import Lower
# Create your views here.

def retrieve_view(request):
    employees = Employee.objects.order_by(Lower('ename')) #Sort by name including lower case
    #To Display Perticular Colums
    #employees = Employee.objects.all().values('ename','esalary')

    #For Insert Data
    #e = Employee.objects.create(eno=100,ename='SOURABH',esalary=90000,eaddress="MAHAJANAPETH").save()

   #For Delete Database Entries
    #e = Employee.objects.get(ename="SOURABH").delete()
    #e = Employee.objects.filter(ename="SOURABH").delete()
    #e = Employee.objects.filter(esalary__gt=15000).delete()

    #For Update
    #e = Employee.objects.get(eno=7776)
    #e.name="SOURABH"

    #For Display Data In Order
    #employees = Employee.objects.order_by('eno') #Acending Order
    #employees = Employee.objects.order_by('-esalary')[0:3] #decending Order

    #union operation
    #qs1 = Employee.objects.filter(esalary__lt=15000) #lt===less than
    #qs2 = Employee.objects.filter(ename__endswith='n')
    #employees = qs1.union(qs2)

    # how to implement NOT queries exclude(condition) Except this condition all remaining data will be display
    # how to implement NOT queries exclude(Q~(condition))
    #employees = Employee.objects.exclude(esalary__range=(10000, 50000))
    #employees = Employee.objects.exclude(~Q(esalary__range=(10000, 12000)))

    # how to implement AND queries(Q(condition1)&Q(condition2))
    # how to implement AND queries(condition1,condition2)
    #employees = Employee.objects.filter(Q(esalary__range=(10000, 50000)) & Q(ename__startswith='S'))
    #employees = Employee.objects.filter(esalary__range=(10000, 50000),ename__startswith='S')

    #how to implement OR queries(Q(condition1)|Q(condition2))
    #employees = Employee.objects.filter(Q(esalary__range=(15000,25000))|Q(ename__startswith='S'))
    # how to implement OR queries queryset_1|queryset_2
    #employees = Employee.objects.filter(esalary__range=(15000,25000))|Employee.objects.filter(ename__startswith='S')

    #employees = Employee.objects.filter(esalary__gte=(15000))
    #employees = Employee.objects.filter(esalary__lte=(15000))

    #employees = Employee.objects.filter(ename_exact='Brandy Roth'))
    #employees = Employee.objects.filter(ename_iexact='brandy roth')) #i means Ignore The Case

    #employees = Employee.objects.filter(ename_contains='john'))
    #employees = Employee.objects.filter(ename_icontains='John'))

    #employees = Employee.objects.filter(id__in=[40,41,42,43])

    #employees = Employee.objects.filter(ename__startswith='J' )
    #employees = Employee.objects.filter(ename__istartswith='J' )

    #employees = Employee.objects.filter(ename__endswith='j' )
    #employees = Employee.objects.filter(ename__iendswith='J' )
    my_dict = {'employees':employees}
    return render(request,"index.html",context=my_dict)


def calculations(request):
    avg = Employee.objects.all().aggregate(Avg('esalary'))
    max = Employee.objects.all().aggregate(Max('esalary'))
    min = Employee.objects.all().aggregate(Min('esalary'))
    sum = Employee.objects.all().aggregate(Sum('esalary'))
    count = Employee.objects.all().aggregate(Count('esalary'))
    my_dict = {'avg':avg, 'max':max, 'min':min, 'sum':sum, 'count':count}
    return render(request,"calculations.html",context=my_dict)