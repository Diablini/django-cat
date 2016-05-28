#encoding:utf-8

from django.template.loader import get_template
from django.template import Template, Context, RequestContext
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from userinfo.models import * 
from django.shortcuts import *
from django.core.exceptions import *
from django.http import HttpResponse
from django.contrib.auth import login as userlogin, authenticate
from django.contrib.auth.models import User

# views

def homepage(request):
	t = get_template('homepage.html')
	c = RequestContext(request,{
		'page_title':'Cats.bg',
		})
	html = t.render(c)
	return HttpResponse(html)

def login(request):
	if (request.method == 'POST'):
		form = loginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password) 
			if user is not None:
				if user.is_active:
					userlogin(request, user)
					return redirect('/')
				else: error = 'Потребителят е неактивен'
			else: error = 'Грешна потребителско име или парола'
		else:  error = 'Непозволени символи в потребителско име или парола'
		form = loginForm()
		t = get_template('login.html')
		c = RequestContext(request,{
			'form':form,
			'error': error,
			})
		html = t.render(c)
		return HttpResponse(html)
		
	else:
		form = loginForm()
		t = get_template('login.html')
		c = RequestContext(request,{
			'form':form,
			'error':'',
			})
		html = t.render(c)
		return HttpResponse(html)


def registration(request):
	if (request.method == 'POST'):
		form = registrationForm(request.POST)
		if form.is_valid:
			username = request.POST['username']
			password = request.POST['password']
			email = request.POST['email']
			user = User.objects.create_user(username=username, \
					password=password, email=email)
			return redirect('/')
		else: 
			error = 'Невалидни данни'
			return redirect('/')
	else:
		form = registrationForm()
		t = get_template('registration.html')
		c = RequestContext(request,{
			'form': form,
			})
		html = t.render(c)
		return HttpResponse(html)


	

	
	
	
		
		