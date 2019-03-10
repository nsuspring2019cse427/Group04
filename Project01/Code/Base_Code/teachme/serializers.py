#!/usr/bin/python

from rest_framework import serializers



from .models import teachers , students


class TeachersSerializer(serializers.ModelSerializer):
	
	
	class Meta:
		model = teachers
		
		
		
		
		
		fields='__all__'
		
		
		
		
class StudentsSerializer(serializers.ModelSerializer):
	
	
	
	class Meta:
		model = students
		
		
		fields='__all__'