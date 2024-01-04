from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    permission = models.IntegerField()
    def __str__(self):
        return f'{self.id} {self.username} {self.password} {self.name} {self.permission}'
