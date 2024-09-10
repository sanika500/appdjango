# from django.db import models
# class details (models.Model):
#name=models.CharField(max_length=225)

from django.db import models
class  details(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    


