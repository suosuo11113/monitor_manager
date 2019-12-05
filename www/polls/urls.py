#!/usr/bin/env python
#_*_ coding:utf-8 _*_


from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.index,name='index'),
    url('(\d{1,10})/detail/$',views.detail,name='detail'),
    url('(\d{1,10})/results/',views.results,name='result'),
    url('(\d{1,10})/vote/',views.vote,name='vote'),

]
