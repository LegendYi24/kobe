from django.db import models

# Create your models here.
class Doctors(models.Model):
    def __str__(self):
        return self.uname
    class Meta:
        db_table = 'Doctors'
        verbose_name = '医生'
        verbose_name_plural = verbose_name
    Mon = '1'
    Tue = '2'
    Wed = '3'
    Thu = '4'
    Fri = '5'
    Sat = '6'
    Sun = '7'
    WORKDAY_CHOICES = (
        (Mon, '星期一'), (Tue, '星期二'), (Wed, '星期三'),
        (Thu, '星期四'), (Fri, '星期五'), (Sat, '星期六'), (Sun, '星期天'),
    )
    CLIENT_CHOICES = (
        ('1','内科'), ('2','五官科'), ('3','神经科'),
        ('4','骨科'), ('5','分泌科'), ('6','外科'),
    )
    uname = models.CharField(max_length=15,verbose_name='医生姓名')
    account = models.CharField(max_length=15,verbose_name='登录账号',unique=True)
    upwd = models.CharField(max_length=12,verbose_name='登录密码')
    workday = models.CharField(max_length=15,verbose_name='值班时间',
                               choices=WORKDAY_CHOICES,default=Mon)
    client = models.CharField(max_length=15,verbose_name='科室',
                              choices=CLIENT_CHOICES,default='1')


class Line(models.Model):
    class Meta:
        db_table = 'Line'
    pat_name = models.CharField(max_length=15,null=True)
    pat_id = models.CharField(max_length=18)
    pat_phone = models.CharField(max_length=11)
    client = models.CharField(max_length=10,null=True)


