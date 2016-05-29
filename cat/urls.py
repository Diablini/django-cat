from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
	url(r'^$', views.homepage),
	url(r'^login/$', views.login),
	url(r'^logout/$', views.logout),
	url(r'^profile/$', views.profile),
	url(r'^registration/$', views.registration),
	url(r'^admin/', include(admin.site.urls) ),
)

