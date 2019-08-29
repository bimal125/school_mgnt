from django.db import models
from schools.models import School
# Create your models here.
class Student(models.Model):
  fname = models.CharField(max_length=20)
  lname = models.CharField(max_length=20)
  roll = models.CharField(max_length=20, unique=True)
  school = models.ForeignKey(School, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)