from django.db import models

# Create your models here.

class Contact(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.CharField(max_length=100)
    Subject=models.CharField(max_length=200)
    Message=models.TextField()

    def __str__(self):
        return self.Name