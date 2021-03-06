from django.shortcuts import render
from fapp.models import FilterModel

# Create your views here.
def upper_view(request):
    data_list = FilterModel.objects.all()
    my_dict = {"data_list":data_list}
    return render(request, "upper.html", context=my_dict)