
#encoding:utf-8

from django.db import models

# Create your models here.


class pet(models.Model):
	name = models.CharField(max_length = 32, unique=False, blank=False)

	owner = models.ForeignKey('myUser', on_delete=models.CASCADE, blank=False, null=False)

	# a list of animal options
	ANIMAL_TYPES = (
		('cat', 'Котка'),
		('dog', 'Куче'),
		('otro', 'Друго'),
	)
	animal_type = models.CharField(max_length = 4, blank=False, choices=ANIMAL_TYPES)
	 
	age = models.DateField(blank=False)
	
	# gender
	GENDER_CHOICES = (
		(True, 'Мъжки'),
		(False, 'Женски'),
	)
	gender = models.BooleanField(blank=False, null=False, choices=GENDER_CHOICES)

	breed = models.CharField(max_length=32)
	# TODO: also add animal class
	

	


	# automatic create and update fields
	date_created = models.DateField(auto_now_add=True)
	date_modified = models.DateField(auto_now=True)

class petPicture(models.Model):

	# title of the image
	title = models.CharField(max_length = 32, null=True)

	# image handle
	img = models.ImageField()

	# pet it belongs to
	src = models.ForeignKey('pet', on_delete=models.CASCADE, blank=False, null=False)

class petPictureComment(models.Model):

	# picture this is a comment to
	src = models.ForeignKey('petPicture', on_delete=models.CASCADE, blank=False, null=False)

	# user that posted it
	usr = models.ForeignKey('User', on_delete=models.CASCADE , blank=False, null=False)

	# date of posting
	date = models.DateTimeField(auto_now_add=True)

	# comment itself
	text = models.CharField(max_length = 512, null=False)
		
	



