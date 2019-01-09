from django.db import models

# Create your models here.
from django.db import models
class student(models.Model):
    Name = models.CharField(max_length=30)#姓名
    Number = models.CharField(max_length=100)#学号
    Age = models.CharField(max_length=50)#年龄
    Origin= models.CharField(max_length=50)#籍贯
    Learn= models.CharField(max_length=100)#专业
    Class = models.CharField(max_length=50)#班级
    def __unicode__(self):
        return self.name
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
