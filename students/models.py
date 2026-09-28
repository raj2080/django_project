from django.db import models

#not raw sql querry, its orm object relation mapping. 

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  age = models.IntegerField()
  address = models.CharField(max_length=200)

  #string representation of a class
  def __str__(self):
    return f"{self.id} {self.name} {self.age}"