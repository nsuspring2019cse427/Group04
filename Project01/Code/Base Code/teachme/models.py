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
		return self.Spost[:50]
		
	


	
	
	

class Project(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True, blank=True)
	budget = models.IntegerField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Project, self).save(*args, **kwargs)

	@property
	def budget_left(self):
		expense_list = Expense.objects.filter(project=self)
		total_expense_amount = 0
		for expense in expense_list:
			total_expense_amount += expense.amount

		# temporary solution, because the form currently only allows integer amounts
		total_expense_amount = int(total_expense_amount)

		return self.budget - total_expense_amount






    @property
    def total_transactions(self):
        expense_list = Expense.objects.filter(project=self)
        return len(expense_list)

    def get_absolute_url(self):
        return '/' + self.slug


class Category(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Expense(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-amount',)

	
	
