from django.db import models
from django.urls import reverse

class Book(models.Model):
  Book_Id = models.IntegerField()
  Title = models.CharField(max_length=100)
  Author = models.CharField(max_length=100)
  Number_of_book = models.IntegerField()
  # Content = models.CharField(max_length=1000)
  

  def __str__(self):
    return self.Title

  def get_absolute_url(self):
    return reverse('book_detail', kwargs={'pk':self.pk})



class Student(models.Model):
  Student_ID = models.IntegerField()
  Name = models.CharField(max_length=100)  
  # issued_date = models.DateField()
 
  def __str__(self):
    return self.Name
