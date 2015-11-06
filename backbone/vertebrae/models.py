from django.db import models
from django.core.validators import MaxLengthValidator

# Create your models here.
class ToDoItem(models.Model):
	title = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)

class Product(models.Model):
	sku = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=11, decimal_places=4, default=0)
	description = models.CharField(max_length=8000)