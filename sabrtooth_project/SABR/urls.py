from django.conf.urls import patterns, url
from SABR import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^player/(?P<playerid>[\w\-]+)/$', views.player, name='player'),
      #  url(r'^search-form/$', views.search_form),
        url(r'^search/$', views.search),
       
        
        
        
        

        
        )
        
        