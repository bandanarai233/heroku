from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView 

from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse_lazy


from .models import Book
from library.forms import BookUpdateForm, BookDeleteForm


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


# class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Book
#     fields = ['Book_Id', 'Title', 'Author', 'Number_of_book']

#     def form_valid(self, form):
#         form.instance.Author = self.request.user
#         return super().form_valid(form)

#     def test_func(self):
#         book = self.get_object()
#         if self.request.user == book.Author:
#             return True
#         return False

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    fields = ['Book_Id', 'Title']

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.Author:
            return True
        return False




# def home(request):
#     context = {
#         'book': Book.objects.all()
#     }
#     return render(request, 'blog/home.html', context)



def rules(request):
    return render(request, 'blog/rules.html', {'Title': 'Rule'})


def form(request):
    return render(request, 'blog/form.html', {'Title': 'Form'})


# def book_detail(request):
#     return render(request, 'blog/book_detail.html')


# def book_update(request):
#     if request.method == 'POST':
#         form = BookUpdateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # form.save(force_insert=False, force_update=False, using=None)
#             print('updated')
#             messages.success(request, f'updated!')
#             return redirect('home')
#         else:
#            messages.error(request, f'cannot be updated!') 
#     else:
#         form = BookUpdateForm()
#         return render(request, 'blog/book_update.html', {'form':form})

# def book_delete(request):
#     if request.method == 'POST':
#         form = BookUpdateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # form.save(force_insert=False, force_update=False, using=None)
#             print('updated')
#             messages.success(request, f'updated!')
#             return redirect('home')
#         else:
#            messages.error(request, f'cannot be updated!') 
#     else:
#         form = BookUpdateForm()
#         return render(request, 'blog/book_delete.html', {'form':form})   




            
   


