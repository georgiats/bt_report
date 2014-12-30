from django.conf.urls import patterns, url

from report import views

urlpatterns = patterns('',
	#url(r'^$', views.home, name='home'),
    #url(r'^(?P<iTravel>\d+)', views.home, name='home'),
    url(r'^$', views.home, name='home'),
   # url(r'^all', views.all, name='all'),
    url(r'^full', views.full, name='full'),
    url(r'^nikos', views.nikos, name='nikos '),
)


