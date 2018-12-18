from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^area1/$', views.area1),
    url(r'^province/$', views.province),
    url(r'^city_(\d+)/$', views.city),
    url(r'^county_(\d+)/$', views.county),
]