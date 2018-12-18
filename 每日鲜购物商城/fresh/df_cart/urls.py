from django.conf.urls import  url
from .views import *

urlpatterns=[
    #显示
    url(r'^$',cart, name='cart'),
    #新增
    url(r'^add/(\d+)/(\d+)/$', add, name='add'),
    url(r'^edit/(\d+)/(\d+)$', edit),
    url(r'^delete/(\d+)$', delete),
    url(r"^cart/$",cart)
]