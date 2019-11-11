from django.contrib import admin
from library.models import Book, Student

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'Title', 'Author', 'Number_of_book']

admin.site.register(Book, BookAdmin)
admin.site.register(Student)
