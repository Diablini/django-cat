#encoding: utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views
from userinfo import views as userviews
from pet import views as petviews

urlpatterns = patterns('',

	url(r'^$', views.homepage),

	# user views
	url(r'^login/$', userviews.login),
	url(r'^logout/$', userviews.logout),
	url(r'^profile/$', userviews.profile),
	url(r'^registration/$', userviews.registration),

	# pet views
	url(r'^pet/create$', petviews.create_pet),

	# admin views
	url(r'^admin/', include(admin.site.urls) ),
)

