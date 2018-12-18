from django.conf.urls import url
from . import views
urlpatterns=[
    url(r"^index/$",views.index,name="index"),
    url(r"^(\d+)/$",views.detail,name="detail"),
    url(r"^list/(\d+)/(\d+)/(\d+)/$",views.list,name="list"),
    url(r"^find/$",views.find,name="find"),
    url(r"^count$",views.cart_count,name='cart_count'),
    url(r"^luck/$",views.luck,name='luck'),
]