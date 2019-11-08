from django.db import models



class Book(models.Model):
  Book_Id = models.IntegerField()
  Title = models.CharField(max_length=100)
  Author = models.CharField(max_length=100)
  Number_of_book = models.IntegerField()
  Available = models.BooleanField()

  def __str__(self):
    return self.Title



class Student(models.Model):
  Student_ID = models.IntegerField()
  Name = models.CharField(max_length=100)  
  # issued_date = models.DateField()
 
  def __str__(self):
    return self.Name