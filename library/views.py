from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse_lazy


from .models import Book
from library.forms import BookUpdateForm, BookCreateForm


# Create your views here.

book = [
    {
        'Book_Id':'2',
        'Title':'Priye Sufi',
        'Author':'Subin Bhattarai',
        'Number_of_book':'15',
        
    },

    {
        'Book_Id':'4',
        'Title':'Mansoon',
        'Author':'Subin Bhattarai',
        'Number_of_book':'5',
       
    }
    
]




class BookListView(ListView):
    model = Book
    template_name = 'blog/home.html'
    context_object_name = 'book'
    # ordering = ['id']


class BookDetailView(DetailView):
    model = Book
    template_name = 'blog/book_detail.html'
    context_object_name ='book'


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookUpdateForm
    template_name = 'blog/book_update.html'
    success_url = reverse_lazy('book_list')



class BookDeleteView(DeleteView):
    model = Book
    template_name = 'blog/book_delete.html'
    success_url = reverse_lazy('book_list')

class BookCreateView(CreateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'blog/book_create.html'
    success_url = reverse_lazy('book_list')


def rules(request):
    return render(request, 'blog/rules.html')


    