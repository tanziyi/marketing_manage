from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    telephone = models.CharField(max_length=11, null=True, unique=True)
    avatar = models.FileField(upload_to='avatars/', default="avatars/default.png")
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    customer = models.ForeignKey(verbose_name='推荐客户', to='Customer', to_field='nid', on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.username

class Customer(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=12)
    age = models.IntegerField()
    email = models.EmailField(null=True, unique=True)
    company = models.CharField(max_length=12)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __str__(self):
        return self.name

