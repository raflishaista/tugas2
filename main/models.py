from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    name2 = models.CharField(max_length=255)
    amount2 = models.IntegerField()
    description2 = models.TextField()
    namaaplikasi = models.TextField()
    nama = models.TextField()
    kelas = models.TextField()
# Create your models here.
