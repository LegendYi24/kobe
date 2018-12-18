from django.db import models
from uuid import uuid1
# Create your models here.
class UserInfo(models.Model):
    id = models.CharField(primary_key=True, default=uuid1().hex, max_length=50) #id
    uname = models.CharField(max_length=20,unique=True)                         #用户名
    user = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)                                      #密码
    uemail = models.EmailField()                                                #邮箱
    ureceive = models.CharField(max_length=100,default="")                      #收货地址
    uaddress = models.CharField(max_length=100,default="")                      #个人地址
    uzipcode = models.CharField(max_length=6,default="")                        #邮编
    uphone = models.CharField(max_length=11,default="")                         #手机号码
    def __str__(self):
        return self.uname
