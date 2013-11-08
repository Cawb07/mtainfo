'''
Created on Nov 7, 2013

@author: Cawb07
'''
from django.conf.urls import patterns, url
from mtainfo import views

urlpatterns = patterns('',
    url(r'^$', views.choice, name='choice'),
)