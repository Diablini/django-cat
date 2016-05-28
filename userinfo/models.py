# encoding:utf-8

from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

# MODELS

class myUser(models.Model):
	userid = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE )
	phonenumber = models.CharField(max_length = 16, blank=True, null=True)
	
	
	def clean(self):
		# FIXME: validate properly
		if not match( r'088\d\d\d\d\d\d\d', self.phonenumber,flags=0):
			raise ValidationError(_('Невалиден телефонен номер'))

# FORMS

class loginForm(forms.Form):
	username = forms.CharField(label='Потребителско име', max_length = 30, required=True)
	password = forms.CharField(label='Парола', widget=forms.PasswordInput, max_length = 30, required=True)
#FIXME: validation

class registrationForm(forms.Form):
	username = forms.CharField(label='Потребителско име', max_length = 30, required=True)
	password = forms.CharField(label='Парола', widget=forms.PasswordInput, max_length = 30, required=True)
	# passwordRepeat = forms.CharField(label='Повторете паролата', widget=forms.PasswordInput, max_length = 30, required=True)
	email = forms.EmailField(required=False)
		
#FIXME: validation


	
	
	
