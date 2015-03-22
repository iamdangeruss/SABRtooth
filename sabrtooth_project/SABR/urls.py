from django.conf.urls import patterns, url
from SABR import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))