from django.shortcuts import render
import datetime
# Create your views here.
def dateTimeInfo(request):
    dateTime = datetime.datetime.now()
    name = "SouRabh"
    hours = int(dateTime.strftime('%H'))
    if hours<12:
        msg = "Good Morning!!!"
    elif hours<16:
        msg = "Good AfterNoon!!!"
    elif hours<22:
        msg = "Good Evening!!!"
    else:
        msg = "Good Night!!!"
    my_dict = {'date': dateTime, 'name': name, 'msg': msg}
    return render(request, "wish.html", context=my_dict)