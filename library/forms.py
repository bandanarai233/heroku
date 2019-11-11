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


# def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Save book'))
#         return render(request, 'blog/book_update.html', {'forms':forms})


class BookDeleteForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('Book_Id', 'Title')


def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save book'))
        return render(request, 'blog/book_delete.html', {'forms':forms})  

    

   

