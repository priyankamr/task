from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accounts/login/$', views.login, name='account_login'),
    url(r'^company_list/$',views.company_list,name="company_list"),
    url(r'^company_add/$',views.company_add,name="company_add"),
    url(r'^company_detail/(?P<id>\d+)/$',views.company_detail,name="company_detail"),
    url(r'^company_edit/(?P<id>\d+)/$',views.company_edit,name="company_edit"),
    url(r'^company_delete/(?P<id>\d+)$',views.company_delete,name="company_delete"),

]

