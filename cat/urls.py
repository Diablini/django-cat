#encoding: utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views
from userinfo import views as userviews
from pet import views as petviews

urlpatterns = patterns('',

	url(r'^$', views.homepage, name = 'home'),

	# user views
	url(r'^login/$', userviews.login, name = 'login'),
	url(r'^logout/$', userviews.logout, name = 'logout'),
	url(r'^profile/$', userviews.profile, name = 'profile'),
	url(r'^registration/$', userviews.registration, name = 'register'),

	# pet views
	url(r'^pet/create$', petviews.create_pet,name = 'createpet'),

	# admin views
	url(r'^admin/', include(admin.site.urls) ),
)

