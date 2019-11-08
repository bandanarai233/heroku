from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

book = [
    {
        'Book_Id':'1',
        'Title':'Priye Sufi',
        'Author':'Subin Bhattarai',
        'Number_of_book':'11',
        'Available':'yes'
    },

    {
        'Book_Id':'2',
        'Title':'Mansoon',
        'Author':'Subin Bhattarai',
        'Number_of_book':'5',
        'Available':'yes'
    }
    
]


def home(request):
    context = {
        'book': book
    }
    return render(request, 'blog/home.html', {'Title': 'Home'}, context)



def rules(request):
    return render(request, 'blog/rules.html', {'Title': 'Rule'})


def form(request):
    return render(request, 'blog/form.html', {'Title': 'Form'})


