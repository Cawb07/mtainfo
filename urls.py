'''
Created on Nov 7, 2013

@author: Cawb07
'''
from django.conf.urls import patterns, url
from fieldtest import views

urlpatterns = patterns('',
    url(r'^$', views.choice, name='choice'),
    url(r'^servicechoice/$', views.servicechoice, name='servicechoice')
)