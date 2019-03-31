#!/usr/bin/python

from django import forms
from .models import *
from django.db import models



class NameForm(forms.Form):
	'''Tname = forms.CharField(label='Tname', max_length=100)'''
	
	
	
	Tname = forms.CharField(label='Tname',max_length=255)
	Tcontact = forms.CharField(label='Tcontact',max_length=255)
	Tarea1 = forms.CharField(label='Tarea1',max_length=255)
	Tarea2 = forms.CharField(label='Tarea2',max_length=255)
	Tgender = forms.CharField(label='Tgender',max_length=255)
	Tmedium = forms.CharField(label='Tmedium',max_length=255)
	
	
	


class SsForm(forms.ModelForm):
	'''Tname = forms.CharField(label='Tname', max_length=100)'''
	
	
	Ssubject = forms.CharField(label='Ssubject',max_length=255)
	Sarea = forms.CharField(label='Sarea',max_length=255)
	Smoney = forms.CharField(label='Smoney',max_length=255)
	Smedium = forms.CharField(label='Smedium',max_length=255)
	Sgender = forms.CharField(label='Sgender',max_length=255)
	Scontact  = forms.CharField(label='Scontact',max_length=255)


	class Meta:
		model=students
		fields=['Ssubject',]
    



	
class Search(forms.Form):
	
	
	
	Tname = forms.CharField(label='Tname',max_length=255)









class CreatePost(forms.ModelForm):


	Spost=forms.CharField(widget=forms.TextInput(),label='Spost',max_length=300)
	
	SofferdMoney=forms.CharField(widget=forms.TextInput(),label='SofferdMoney',max_length=255)
	Ssubject=forms.CharField(widget=forms.TextInput(),label='Ssubject',max_length=255)
		




	class Meta():

		model = StudentPost
		fields=['Spost','SofferdMoney','Ssubject']


