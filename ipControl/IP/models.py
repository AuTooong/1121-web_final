from django.db import models

# Create your models here.

class IP(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=20)
    service = models.CharField(max_length=20)
    product = models.CharField(max_length=20)
    os = models.CharField(max_length=20)
    unix_like = models.BooleanField()
    owner = models.ForeignKey("Owner",
                              on_delete=models.PROTECT)
    def __str__(self):
        return f"{self.id} {self.ip} {self.service} {self.product} {self.os} {self.unix_like} {self.owner}"

class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    ext = models.IntegerField()
    def __str__(self):
        return f"{self.id} {self.name} {self.unit} {self.ext}"
