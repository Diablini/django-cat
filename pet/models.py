
#encoding:utf-8

from django.db import models

# Create your models here.


class petInfo(models.Model):
	name = models.CharField(max_length = 64, unique=False, blank=False)

	# a list of animal options
	ANIMAL_TYPES = (
		('cat', 'Котка'),
		('dog', 'Куче'),
		('otro', 'Друго'),
	)

	animal_type = models.CharField(max_length = 4, blank=False, choices=ANIMAL_TYPES)
	# 
	age = models.DateField()

	free_text = models.CharField(max_length = 1024, blank=True, null=True)
	date_published = models.DateField(auto_now_add=True)
	date_modified = models.DateField(auto_now=True)



