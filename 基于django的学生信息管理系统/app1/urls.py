from django.conf.urls import url

from app1 import views

urlpatterns=[
    url(r'^url_hello/',views.hello),
    url(r'^url_done/',views.addstu),
    url(r'^url_check/',views.checkstu),
    url(r'^url_rewiter/',views.rewirte),
    url(r'^url_delet/',views.deletestu),

    url(r'^url_studentinfo/(\d+)/$', views.studentinfo, name='url_studentinfo'),
    url(r'^url_login',views.login),
    url(r'^url_regist/', views.regist),


]