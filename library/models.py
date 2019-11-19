from django.db import models
from django.urls import reverse
from phone_field import PhoneField

class Book(models.Model):
  Book_Id = models.IntegerField()
  Title = models.CharField(max_length=100)
  Author = models.CharField(max_length=100)
  Number_of_book = models.IntegerField()
  

  def __str__(self):
    return self.Title

  def get_absolute_url(self):
    return reverse('book_detail', kwargs={'pk':self.pk})



class Student(models.Model):
  Name = models.CharField(max_length=100)  
  Class = models.IntegerField(null=True, blank=True)
  Email = models.EmailField(blank=True, null=True)
  Contact = PhoneField(blank=True, help_text='Contact phone number')
 
  def __str__(self):
    return self.Name
