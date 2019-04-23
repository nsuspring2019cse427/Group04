#!/usr/bin/python

from django.test import TestCase , Client
from django.urls import reverse
from teachme.models import Project , Category ,  Expense
import json






class TestViews(TestCase):


	def setUp(self):
		self.client = Client()
		self.list_url = reverse('list')
		self.detail_url = reverse('detail' , args=['project1'])
		self.project1 = Project.objects.create(name = 'project1' , budget = 10000)





		


	def test_project_list_GET(self):


		right_Status_code = 200
		false_status_code = 000
		error_code = 404

		response = self.client.get(self.list_url)

		self.assertEquals(response.status_code,right_Status_code)
		self.assertNotEquals(response.status_code , false_status_code)
		self.assertTemplateUsed(response, 'budget_study.html')





	def test_project_using_false_urls(self):


		right_Status_code = 200
		false_status_code = 000
		error_code = 404

		response = self.client.get("something/False")

		
		self.assertNotEquals(response.status_code , false_status_code)
		self.assertEquals(response.status_code , error_code)









	def test_Project_details_get(self):


		right_Status_code = 200
		false_status_code = 000
		error_code = 404


		response = self.client.get(self.detail_url)

		self.assertEquals(response.status_code,right_Status_code)
		self.assertTemplateUsed(response, 'project-detail.html')
		self.assertNotEquals(response.status_code , false_status_code)
		self.assertNotEquals(response.status_code , error_code)




	def test_false_details_url(self):
		right_Status_code = 200
		false_status_code = 000
		error_code = 404
		


		response = self.client.get("falseDtails/url")
		self.assertNotEquals(response.status_code , false_status_code)
		self.assertEquals(response.status_code , error_code)













	def test_project_detail_POST_adds_new_expense(self):

		Category.objects.create(
			project=self.project1 ,
			name = 'development'
		)


		response = self.client.post(self.detail_url , {

			'title' : 'expense1' ,
			'amount' : 10000 ,
			'category' : 'development'
		})


		right_Status_code = 302
		false_status_code = 000
		error_code = 404
		right_title = "expense1"

		self.assertEquals(response.status_code , right_Status_code)
		self.assertNotEquals(response.status_code , false_status_code)
		self.assertEquals(self.project1.expenses.first().title , right_title)




	def test_project_detail_POST_adds_Wrong_expense_will_result_error(self):

		
		actual_money = 1999
		actual_title = 'expense1'
		actual_category = 'development'
		
		Category.objects.create(
			project=self.project1 ,
			name = 'development'
		)


		response = self.client.post(self.detail_url , {

			'title' : actual_title ,
			'amount' : actual_money ,
			'category' : actual_category
		})


		right_Status_code = 302
		false_status_code = 000
		error_code = 404
		right_title = "expense1"
		right_amount = actual_money
		wrong_amount = 12122
		






		self.assertEquals(response.status_code , right_Status_code)
		self.assertEquals(self.project1.expenses.first().title , right_title)
		self.assertEqual(self.project1.expenses.first().amount, right_amount )
		self.assertTrue(self.project1.expenses.first().amount, right_amount)


		




		self.assertEquals(response.status_code , right_Status_code)

		print(self.project1.expenses.first().amount)
		
		
		
		
		
		
		
	














	def test_project_detail_POST_no_deta(self):
		response = self.client.post(self.detail_url)
		self.assertEquals(response.status_code,302)
		print("till done 2")
		self.assertEquals(self.project1.expenses.count(), 0)
		print("till done 3")




	def test_project_detail_DELETE_deletes_expense(self):


		category1 = Category.objects.create(
			project=self.project1 ,
			name = 'development'
		)



		Expense.objects.create(
			project = self.project1,
			title='expense1',
			amount=1000,
			category = category1
		)



		response = self.client.delete(self.detail_url, json.dumps({'id':1}))

		self.assertEqual(response.status_code, 204)
		self.assertEqual(self.project1.expenses.count(),0)




	def test_project_create_POST(self):

		url=reverse('add')
		responce = self.client.post(url ,{
		'name':'project2',
		'budget': 10000,
		'categoriesString': 'design,development'
		})


		project2 = Project.objects.get(id=2)
		self.assertEqual(project2.name, 'project2')
		first_category = Category.objects.get(id=1)
		self.assertEqual(first_category.project , project2)
		self.assertEqual(first_category.name, 'design')
		second_category = Category.objects.get(id=2)
		self.assertEqual(second_category.project , project2)
		self.assertEqual(second_category.name, 'development')






class testIntegrations(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/teachme/')
        self.assertEquals(response.status_code, 200)


    def test_home_to_signup(self):
    	response = self.client.get('/teachme/signin/')
    	self.assertEquals(response.status_code, 200)

   

    def test_home_to_teacher_signin(self):
    	response = self.client.get('/teachme/signin/')
 		self.assertEquals(response.status_code, 200)


 	def test_home_to_student_signin(self):

		response = self.client.get('/teachme/student_signin/')
 		self.assertEquals(response.status_code, 200)

 	def test_teacherLogIn_to_TeacherProfile(self):
 		response = self.client.get('/teachme/profile/')
 		self.assertEquals(response.status_code, 200)

 	def test_TeacherProfile_to_tlist(self):
 		response = self.client.get('/teachme/profile/t_list')
 		self.assertEquals(response.status_code, 200)


	def test_TeacherProfile_to_post(self):
 		response = self.client.get('/teachme/profile/studentPostList/')
 		self.assertEquals(response.status_code, 200)

 	def test_teacherProfile_to_logOut(self):
 		response = self.client.get('/teachme/profile/logout/')
 		self.assertEquals(response.status_code, 404)

 	def studentSignIn_to_studentProfile(self):
 		response = self.client.get('/teachme/student_profile/')
 		self.assertEquals(response.status_code, 200)

 	def test_student_profile_to_tlist(self):
 		response = self.client.get('/teachme/student_profile/t_list/')
 		self.assertEquals(response.status_code, 200)

 	def test_student_profile_to_createPost(self):
 		response = self.client.get('/teachme/student_profile/createPost/')
 		self.assertEquals(response.status_code, 200)

 	def test_student_profile_to_budget(self):
 		response = self.client.get('/teachme/student_profile/budget_study/')
 		self.assertEquals(response.status_code, 200)

    

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/teachme/')
        self.assertContains(response, '<h1>শিক্ষক দিচ্ছি-নিচ্ছি!</h1>')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/teachme/')
        self.assertNotContains(
            response, 'Hi there! You should not be on the page.')






		
