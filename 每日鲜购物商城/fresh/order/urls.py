from django.conf.urls import url
from . import views
urlpatterns=[
    #购物车提交订单
    url(r'^$',views.order, name='order'),
    #新增订单
    url(r'^order_handle/$', views.order_handle, name='order_handle'),
    url(r'^order_list(\d*)$', views.order_list, name='order_list'),
    #显示付款
    url(r'^pay(\w*)', views.pay, name='pay'),
    #显示订单
    url(r'^show(\d*)/$',views.show,name="show"),
    #显示支付
    url(r'^gert', views.gert, name='gert'),
]
