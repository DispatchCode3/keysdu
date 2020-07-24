import math
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe

class State(models.Model):
	abbreviation = models.CharField(max_length=5, unique=True)
	name = models.CharField(max_length=30)
		
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "State"
		verbose_name_plural = "States"

class County(models.Model):
	name = models.CharField(max_length=30, unique=True)
	state = models.ForeignKey(State, related_name='counties', on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "County"
		verbose_name_plural = "Counties"

class City(models.Model):
	name = models.CharField(max_length=30, unique=True)
	county = models.ForeignKey(County, related_name='cities', on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name
		
	class Meta:
		verbose_name = "City"
		verbose_name_plural = "Cities"

class Address(models.Model):
	area = models.CharField(max_length=3, blank=True, null=True)
	number = models.CharField(max_length=6)
	directional = models.CharField(max_length=1, blank=True, null=True)
	street_name = models.CharField(max_length=50)
	street_type = models.CharField(max_length=15, blank=True, null=True)
	suffix = models.CharField(max_length=1, blank=True, null=True)
	zipcode = models.CharField(max_length=10, blank=True, null=True)
	city = models.ForeignKey(City, related_name='addresses', on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Address"
		verbose_name_plural = "Addresses"
