from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views
from userinfo import views as userviews

urlpatterns = patterns('',
	url(r'^$', views.homepage),
	url(r'^login/$', userviews.login),
	url(r'^logout/$', userviews.logout),
	url(r'^profile/$', userviews.profile),
	url(r'^registration/$', userviews.registration),
	url(r'^admin/', include(admin.site.urls) ),
)

