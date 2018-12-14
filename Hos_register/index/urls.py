from django.conf.urls import url,include
from .views import *

urlpatterns = [
    url('^$',index_views),
    url(r'^doc_login/$',doc_login_views),
    url(r'^pat_login/$',pat_login_views),
    url(r'^cancel_login/$',cancel_login_views),
    url(r'^query_line/$',query_line_views),
    url(r'^login_out/$',doc_loginout_views),
    url(r'^show_line/$',show_line_views),
    url(r'^next_pat/$',next_pat_views),
]

urlpatterns += [
    url(r'^about/$',about_views),
    url(r'^team/$',team_views),
]
