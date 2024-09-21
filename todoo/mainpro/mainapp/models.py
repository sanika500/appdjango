from django.db import models

# Create your models her
class details(models.Model):
    todo=models.CharField(max_length=100)
