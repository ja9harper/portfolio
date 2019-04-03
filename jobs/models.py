from django.db import models

# Create your models here.
class Job(models.Model):
    #Images will be saved
    image = models.ImageField(upload_to='images/')
    #summary set to 200 characters
    summary = models.CharField(max_length=200)
