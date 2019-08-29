from django.db import models

# Create your models here.
class School(models.Model):
  name = models.CharField(max_length=20)
  max_students = models.PositiveIntegerField(null=True,blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)