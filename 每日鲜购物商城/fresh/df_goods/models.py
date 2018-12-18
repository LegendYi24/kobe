from django.db import models
from tinymce.models import HTMLField


class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20, unique=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle


class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20, unique=True)  # 标题
    gpic = models.ImageField(upload_to='images/goods')  # 图片
    gprice = models.DecimalField(max_digits=5, decimal_places=2)  # 价格
    gunit = models.CharField(max_length=20, default='500g')  # 单位
    gclick = models.IntegerField(default=0)  # 点击量
    gintroduction = models.CharField(max_length=200)  # 简介
    gstock = models.IntegerField(default=0)  # 库存
    gcontect = HTMLField()  # 内容
    gtypeinfo = models.ForeignKey(TypeInfo)  # 所属类型
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return self.gtitle