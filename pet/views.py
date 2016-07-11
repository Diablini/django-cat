# encoding:utf-8

from django.shortcuts import render, redirect
from django.template.loader import get_template
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
		form = petForm(request.POST, initial = {'owner': request.user.id})
		if form.is_valid():
			form.save()
			return redirect('/')
		else: raise PermissionDenied('fack')
	else:
		form = petForm(data = {'owner': request.user.id })
		t = get_template('pet_create.html')
		c = RequestContext(request,{
			'form': form,
			})
		html = t.render(c)
		return HttpResponse(html)
	
