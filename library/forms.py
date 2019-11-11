from django import forms
from django.shortcuts import render
from django.http import request
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from library.models import Book


class BookUpdateForm(forms.ModelForm):
        class Meta:
                model = Book
                fields = ('Title', 'Number_of_book')
                

class BookCreateForm(forms.ModelForm):
        class Meta:
                model = Book
                fields = ('Book_Id', 'Title', 'Author', 'Number_of_book')