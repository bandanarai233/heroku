from django.contrib import admin
from library.models import Book, Student

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'Title', 'Author', 'Number_of_book']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Class', 'Email', 'Contact']

    def student_info(self, obj):
        return obj.Name

admin.site.register(Book, BookAdmin)
admin.site.register(Student, StudentAdmin)



