from django.db import models

# Create your models here.

class IP(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=20)
    service = models.CharField(max_length=20)
    product = models.CharField(max_length=20)
    os = models.CharField(max_length=20)
    unix_like = models.CharField(max_length=20)
    owner_id = models.IntegerField()
    def __str__(self):
        return self.ip
