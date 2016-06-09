# encoding:utf-8

from django.shortcuts import render
from django.template import Template, Context, RequestContext
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from models import *

# Create your views here.

def create_pet(request):
	if not request.user.is_authenticated():
		raise PermissionDenied('Само логнати потребители\
					могат да създават профили')
	if (request.method == 'POST'):
		return
	else:
		html = ' '
		return HttpResponse(html)
	
