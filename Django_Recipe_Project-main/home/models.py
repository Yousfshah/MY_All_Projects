from django.db import models

# Create your models here.

class student(models.Model):
    name= models.CharField(max_length=50)
    age= models.IntegerField(null=True, blank=True)
    email= models.EmailField(null=True, blank=True)
    address= models.TextField(null=True, blank=True)
    phone=models.IntegerField()
class car(models.Model):
    car_name= models.CharField(max_length=150)
    speed= models.IntegerField(default=50)
    
    # def __str__(self) -> str:
    #     return self.car_name