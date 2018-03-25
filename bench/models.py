# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
# Create your models here.
class Category(models.Model):
	category_name=models.CharField(max_length=45)

	def __str__(self): 
		return self.category_name

class Country(models.Model):
	country_name=models.CharField(max_length=50)
	country_code = models.CharField(max_length=50)

	def __str__(self):
		return self.country_name

class Currency(models.Model):
	currency_name = models.CharField(max_length=45)
	currency_code= models.CharField(max_length=45)

	def __str__(self):
		return self.currency_name

class CurrencyName(models.Model):
	token_name=models.CharField(max_length=20)
	price=models.DecimalField(max_digits=5, decimal_places=2)
	platform=models.CharField(max_length=45)
	accepting=models.CharField(max_length=45)
	minimum_investment=models.IntegerField(default=0)
	soft_cap=models.IntegerField(default=0)
	hard_cap=models.IntegerField(default=0)
	country=models.ForeignKey(Country, related_name='+')
	restricted_areas=models.ManyToManyField(Country)
	bonus=models.CharField(max_length=45, blank=True)
	bounty=models.CharField(max_length=45, blank=True)
	Whitelist_KYC=models.CharField(max_length=45, blank=True)

	def __str__(self):
		return self.token_name
		

class Company(models.Model):
	name=models.CharField(max_length=45)
	title=models.CharField(max_length=100)
	description=models.TextField(blank=True, null=True)
	category=models.ManyToManyField(Category)
	video_file = models.FileField(upload_to = 'videos/', max_length=200)
	logo = models.FileField(upload_to='images/')
	start_date = models.DateTimeField(default=now)
	end_date = models.DateTimeField(default=now)
	token  = models.ForeignKey(CurrencyName, related_name="+",default=1)

	def __str__(self): 
		return self.name


class Rating(models.Model):
	company = models.ForeignKey(Company, related_name="+", default=1)
	ico_profile=models.CharField(max_length=25)
	team=models.CharField(max_length=25)
	vision=models.CharField(max_length=25)
	product=models.CharField(max_length=25)
	total_rating = models.IntegerField(default=0,blank=True)

	def __str__(self):
		return self.ico_profile



		
# class UserDetails(models.Model):
# 	your_name = models.CharField(max_length=45)