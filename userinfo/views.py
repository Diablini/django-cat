
#encoding:utf-8

from django.template.loader import get_template
from django.template import Template, Context, RequestContext
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from userinfo.models import * 
from django.shortcuts import *
from django.core.exceptions import *
from django.http import HttpResponse
from django.contrib.auth import login as userlogin, authenticate, logout as userlogout
from django.contrib.auth.models import User

# Create your views here.


def login(request):
	# user has posted login form - validate and login
	if (request.method == 'POST'):
		form = loginForm(request.POST)
		if form.is_valid:
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
		
	# user hasnt posted form
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
	# user has posted registration form - validate
	if (request.method == 'POST'):
		form = registrationForm(request.POST)
		if form.is_valid:
			username = request.POST['username']
			password = request.POST['password']
			email = request.POST['email']
			user = User.objects.create_user(username=username, \
					password=password, email=email)
			# create user profile and bind to django's User
			profile = myUser()
			return redirect('/')
		else: 
			error = 'Невалидни данни'
			return redirect('/')
	# user hasnt posted form - render empty form
	else:
		form = registrationForm()
		t = get_template('registration.html')
		c = RequestContext(request,{
			'form': form,
			})
		html = t.render(c)
		return HttpResponse(html)

def profile(request):
	# assert user is logged in
	if (not request.user.is_authenticated):
		raise PermissionDenied
	# form has been posted - validate and save
	if (request.method == 'POST'):
		form = profileForm(request.POST, instance=request.user.profile)
		if form.is_valid:
			form.save()
			return redirect('/')
		else:
			error = 'Невалидни данни'
			return redirect('/')
	# form has not been posted - render current profile
	else:
		form = profileForm(instance=request.user.profile)
		t = get_template('profile.html')
		c = RequestContext(request, {
			'form': form,
		})
		html = t.render(c)
		return HttpResponse(html)

def logout(request):
	userlogout(request)
	return redirect('/')



