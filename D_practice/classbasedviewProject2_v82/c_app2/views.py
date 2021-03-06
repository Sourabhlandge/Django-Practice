from django.shortcuts import render
from django.views.generic import ListView,DetailView
from c_app2.models import BookModel

# Create your views here.
class BookListView(ListView):
    model = BookModel
    template_name = 'bookmodel_list.html'
    context_object_name = 'list_of_books'
    #default template name: bookmodel_list.html
    #default context object: bookmodel_list
class BookDetailView(DetailView):
    model = BookModel
    template_name = 'book_detail.html'
    context_object_name = 'book'
    # default template name: bookmodel_detail.html
    # default context object: bookmodel
