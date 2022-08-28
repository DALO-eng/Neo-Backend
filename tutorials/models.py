from django.db import models

# Create your models here.
class Tutorial(models.Model):
    nombre = models.CharField(max_length=70, blank=False, default='')
    cel = models.CharField(max_length=10,blank=False, default='')
    contra = models.CharField(max_length=4,blank=False, default='')
    conf = models.CharField(max_length=4,blank=False, default='')