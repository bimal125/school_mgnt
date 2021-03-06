from django.db import models
from schools.models import School
import uuid 

# Create your models here.
class Student(models.Model):
  fname = models.CharField(max_length=20)
  lname = models.CharField(max_length=20)
  nationality = models.CharField(max_length=20, null=True, blank=True)
  age = models.PositiveIntegerField(null=True, blank=True)
  sex = models.CharField(max_length=20, null=True, blank=True)
  roll_no = models.CharField(max_length=20, unique=True)
  school = models.ForeignKey(School, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def save(self, *args, **kwargs):
      super().save(*args, **kwargs)
      self.roll_no = uuid.uuid4().hex[:20].upper()
      super().save(force_update=True)

  def __str__(self):
      return str(self.fname)

