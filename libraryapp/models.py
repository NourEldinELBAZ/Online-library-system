from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
  name = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  description = models.TextField()
  category = models.CharField(max_length=100)
  cover = models.ImageField()
  is_borrowed = models.BooleanField(default=False)
  borrowed_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='borrowed_books')

  def __str__(self):
    return self.name