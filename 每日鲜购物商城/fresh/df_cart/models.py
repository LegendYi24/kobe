from django.db import models
from df_user.models import UserInfo
from df_goods.models import GoodsInfo
# Create your models here.
class CartInfo(models.Model):
    userinfo=models.ForeignKey(UserInfo)            #用户
    goodsinfo=models.ForeignKey(GoodsInfo)          #商品
    count=models.IntegerField()                     #数量
    isdelete=models.BooleanField(default=False)