from django.db import models
from df_user.models import UserInfo

class OrderInfo(models.Model):
    oid = models.CharField(primary_key=True, max_length=50)
    userinfo=models.ForeignKey(UserInfo)
    odate=models.DateTimeField(auto_now_add=True)
    oispay=models.BooleanField(default=False)
    ototal=models.DecimalField(max_digits=10,decimal_places=2)
    oaddress=models.CharField(max_length=150)
#shanchushangping
class OrderDetailInfo(models.Model):
    goodsinfo=models.ForeignKey('df_goods.GoodsInfo')
    orderinfo=models.ForeignKey(OrderInfo)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    count=models.IntegerField()