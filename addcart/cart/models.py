from django.db import models

class product(models.Model):
    No=models.IntegerField()
    Name=models.CharField(max_length=10)
    Catagory=models.CharField(max_length=10)
    Email=models.EmailField()
    Contact=models.IntegerField()
