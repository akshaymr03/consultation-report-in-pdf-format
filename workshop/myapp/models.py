from django.db import models

# Create your models here.
class home(models.Model):
    clinicName=models.CharField(max_length=100)
    clinicLogo=models.ImageField(upload_to='workshop/logo/')
    physicianName=models.CharField(max_length=100)
    physicianContact=models.CharField(max_length=100)
    pfname=models.CharField(max_length=100)
    plname=models.CharField(max_length=100)
    pdob=models.CharField(max_length=100)
    pcontact=models.CharField(max_length=100)
    complaint=models.CharField(max_length=500)
    consultation=models.CharField(max_length=500)