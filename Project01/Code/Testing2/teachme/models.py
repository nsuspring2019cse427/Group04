# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone



# Create your models here.
class teachers(models.Model):
	Tid = models.CharField(max_length=255)
	Tname = models.CharField(max_length=255)
	Tcontact = models.CharField(max_length=255)
	Tarea1 = models.CharField(max_length=255)
	Tarea2 = models.CharField(max_length=255)
	Tgender = models.CharField(max_length=255)
	Tmedium = models.CharField(max_length=255)
	Tsubject=models.CharField(max_length=225)
	
	
	
	
	def __str__(self):
		return self.Tname
  




class students(models.Model):
	Sname = models.CharField(max_length=255)
	Ssubject=models.CharField(max_length=255)
	Sarea=models.CharField(max_length=255)
	Smoney=models.CharField(max_length=255)
	Smedium=models.CharField(max_length=255)
	Sgender=models.CharField(max_length=255)
	Scontact=models.CharField(max_length=255)
	
	def __str__(self):
		return self.Sname
		
		
		
		
		
		
		
		
		
		
		
		
class StudentPost(models.Model):
	
	Spost=models.CharField(max_length=300)
	SpostedBy=models.CharField(max_length=225)
	SpostTime=models.DateField(default=timezone.now)
	SofferdMoney=models.CharField(max_length=225)
	Ssubject=models.CharField(max_length=225)
	
	
	
	def __str__(self):
		return self.SpostedBy 
		
		
	def __str__(self):
		return self.Spost[:150]
		
	


	
	
	
	'''Spost  SpostedBy  SpostTime   SofferdMoney'''
	
	
