from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^register/$',views.register,name="register"),
    url(r'^register_exist',views.register_exist,name="register_exist"),
    url(r'^login/$',views.login,name="login"),
    url(r'^user_goods/$',views.user_goods,name="user_goods"),
    url(r'^register_handle/$',views.register_handle,name="register_handle"),
    url(r'^login_handle/$', views.login_handle, name="login_handle"),
    url(r'^info/$',views.user_center_info,name="user_center_info"),
    url(r'^order/$',views.user_center_order,name="user_center_order"),
    url(r'^logout/$',views.logout,name="logout"),
    url(r'^site/$',views.user_center_site,name="user_center_site"),
    url(r'^insert/$',views.user_insert,name="user_insert"),
    url(r'^update/$',views.user_update,name="user_update"),
    url(r'^$',views.user_goods,name="user_goods"),
    url(r'^verification$', views.verification, name='verification'),
    url(r'^check_userverification', views.check_userverification, name='check_userverification'),
    url(r'^result$', views.result, name='result'),

]