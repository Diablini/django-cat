# encoding:utf-8

from django import forms
from django.forms import ModelForm
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
import re

# MODELS

class myUser(models.Model):
	userid = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE )
	location = models.CharField(max_length = 64, blank=True, null=True)
	phonenumber = models.CharField(max_length = 16, blank=True, null=True)
	freetext = models.CharField(max_length = 512, blank=True, null = True)
	
	# create a myUser profile linked to a user when a user is created
	@receiver(post_save, sender=User)
	def create_profile(sender, instance, created, **kwargs):
		if (created):
			profile = myUser()
			profile.userid = instance
			profile.save()
		else: return

	def __str__(self):
		return self.userid.username + ' profile'
		
	
	def clean(self):
		# FIXME: validate properly
		if not match( r'088\d\d\d\d\d\d\d', self.phonenumber,flags=0):
			raise ValidationError('Невалиден телефонен номер')

# FORMS

class loginForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']
		labels = {
			'username': 'Име:',
			'password': 'Парола:',
		}
		help_texts = {
			'username': None,
			'password': None,
		}
		widgets = {
			'username': forms.TextInput,
			'password': forms.PasswordInput,
		}
		
#FIXME: validation

class registrationForm(forms.Form):
	username = forms.CharField(label='Потребителско име', max_length = 30, required=True)
	password = forms.CharField(label='Парола', widget=forms.PasswordInput, max_length = 30, required=True)
	passwordRepeat = forms.CharField(label='Повторете паролата', widget=forms.PasswordInput, max_length = 30, required=True)
	email = forms.EmailField(label='Мейл адрес', required=False)
		
#FIXME: validation

class profileForm(ModelForm):
	class Meta:
		model = myUser
		fields = ['location', 'phonenumber', 'freetext']
		labels = {
			'location': 'Местоположение',
			'phonenumber': 'Телефонен номер',
			'freetext': 'Свободен текст',
		}
		help_texts = {
			'location': None,
			'phonenumber': None,
			'freetext': None,
		}
		
#FIXME: validation


	
	
	
