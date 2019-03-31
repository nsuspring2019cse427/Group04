from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout as django_logout
from .models import teachers
from .models import students
from .models import  StudentPost
from django import forms
from .forms import NameForm ,  CreatePost , Search ,SsForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TeachersSerializer , StudentsSerializer
import random



#this is tha main home page indedex
def index(request):
	return render(request, 'index.html')  
def post(request):
	return HttpResponse("<h1> this is post </h1>")


#using django authentication form

def signin(request):
	
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = form.get_user()
			
			login(request, user) 
			
			
			return redirect('/teachme/profile')     #redirecting to profile page    
	else:
		form = AuthenticationForm()
	return render(request, 'signin.html') #if error replace {'form': form}) 
	
	
	
	
	
	

	
	
def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')  # !!!! i used used password 1 method
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('/teachme/set_profile')
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form': form})






def student_signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)  #sending data to authentication 
			login(request, user)
			return redirect('/teachme/set_student_profile')
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form': form})


def student_signin(request):


	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = form.get_user()
			
			login(request, user)
			
			
			return redirect('/teachme/student_profile')        
	else:
		form = AuthenticationForm()
	return render(request, 'student_signin.html') #if error replace {'form': form})
	




def profile(request):
	global teachers 
	teacher=teachers.objects.get(Tname=request.user.username)
	return render(request, 'profile.html',{'teachers': teacher}) #model -> teacher -> base -> page
	

def logout(request):

	
	django_logout(request)    #logout current user
	return redirect('index')
	
	
"""def info(request):
	global teachers 
	teacher=teachers.objects.get(Tname="shifat")
	teacher.Tcontact="362436"
	teacher.save()
	return render(request, 'info.html',{'teachers': teacher})"""







def student_profile(request):
	
	return render(request,'student_profile.html')   #after student login  load this 





def info(request):
	global teachers 
	teacher=teachers.objects.all()
	return render(request, 'info.html',{'teachers': teacher})  #testing if data passing clearly


def s_login(request):

	return render(request, 's_login.html')   #using another login method

def t_list(request):
	
	global teachers 
	teacher=teachers.objects.all()
	return render(request, 't_list.html',{'teachers': teacher})  #listing teachers 




def set_profile(request):
	
	return render(request,'set_profile.html')   # take users info teacher




def set_student_profile(request):
	
	return render(request,'set_student_profile.html')  # take students info





def s_home(request):

	return render(request,'s_home.html')   
	
	




def test1(request,name):
	
	"""return HttpResponse("this is tha profile of:       "   + name )"""
		
	global teachers 
	teacher=teachers.objects.get(Tname=name)
	return render(request, 'test1.html',{'teachers': teacher})  # url data using to filter

	







def singupprocess(request):
	
	
	if request.method == 'POST':
		# create a form instance 
		form = NameForm(request.POST)
		# check whether it's valid:
			 
		if form.is_valid():       
			teachers.objects.create(Tname=form.cleaned_data['Tname'],Tcontact=form.cleaned_data['Tcontact'],Tarea1=form.cleaned_data['Tarea1'],Tarea2=form.cleaned_data['Tarea2'],Tgender=form.cleaned_data['Tgender'],Tmedium=form.cleaned_data['Tmedium'],Tid=random.randint(1000,9999))
			 
			return redirect('index')

	# if a GET  tahole change korbo pore jate shoja namaite pari
	# adding info to database
	else:
		form = NameForm()

	return render(request, 'set_profile.html', {'form': form})







def student_singupprocess(request):
	
	
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = SsForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			print("form is valid")
			students.objects.create(Sname=request.user.username,Ssubject=form.cleaned_data['Ssubject'],Sarea=form.cleaned_data['Sarea'],Smedium=form.cleaned_data['Smedium'],Sgender=form.cleaned_data['Sgender'],Scontact=form.cleaned_data['Scontact'], Smoney=form.cleaned_data['Smoney'])
			 
			return redirect('/teachme/student_profile')
			

	# if a GET 
	else:
		form = SsForm()

	return render(request, 'set_student_profile.html', {'form': form})










def search(request):
	
	
	return render(request, 'search.html')





def searchprocess(request):
	
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = search(request.POST)
		# check whether it's valid:
		if form.is_valid():
			
			 
			return HttpResponse(form.cleaned_data['Tname'])

	# if a GET (or any other method) we'll create a blank form
	else:
		form = search()

	return render(request, 'search.html')
	

def studentPostList(request):   #lists of students post
	
	
	global StudentPost
	post= StudentPost.objects.all()
	return render(request, 'StudentPost.html',{'StudentPost': post})




def back_profile(request):


	return redirect('/teachme/profile')




def createPost(request):

	return render(request,'create_post.html')  #posting page




# storing data from post to database 


def createPostProcess(request):



	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = CreatePost(request.POST)
		# check whether it's valid:
		if form.is_valid():
			StudentPost.objects.create(Spost=form.cleaned_data['Spost'], SpostedBy=request.user.username, SofferdMoney = form.cleaned_data["SofferdMoney"], Ssubject=form.cleaned_data["Ssubject"])
			return redirect('/teachme/student_profile')

	# if a GET 
	else:
		form = CreatePost()

	return render(request, 'create_post.html', {'form': form})
	
	
#rest api ------ !!!!!	
	
class TeachersList(APIView):
	
	                              #transfring data to GET data
	def get(self,request):
		teacher = teachers.objects.all()
		serializer=TeachersSerializer(teacher,many=True)  
		return Response(serializer.data)
	
	                             #recive data 
	def post(self,request):
		teacher = teachers.objects.all()
		serializer=TeachersSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
	
	
	
	
	
class StudentsList(APIView):
		
		
		def get(self,request):
			student = students.objects.all()
			serializer=StudentsSerializer(student,many=True)
			return Response(serializer.data)
		
		
		def post(self,request):
			student = students.objects.all()
			serializer=StudentsSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)

	












def add(x , y):
	return x+y







