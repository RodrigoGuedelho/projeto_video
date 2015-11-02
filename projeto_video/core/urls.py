from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('projeto_video.core.views',
	url(r'^$', 'home', name='home'),
)
