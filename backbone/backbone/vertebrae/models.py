from django.db import models
from django.core.validators import MaxLengthValidator

# Create your models here.
class ToDoItem(models.Model):
	title = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)