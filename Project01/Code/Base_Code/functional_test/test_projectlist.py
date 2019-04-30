from selenium import webdriver
from budget.models import Project
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time





class TestProjectListPage(StaticLiveServerTestCase):



	def setUp(self):

		self.browser = webdriver.Chrome('/Users/shifatahmed_MAC/Downloads/chromedriver')




	def tearDown(self):

		self.browser.close()


	def test_no_project_is_there(self):


		self.browser.get(self.live_server_url)
		


		# user requester the page for the first time 


		


		alert = self.browser.find_element_by_class_name('noproject-wrapper')

		self.assertEquals(alert.find_element_by_tag_name('h3').text , "Sorry, you don't have any projects, yet." )

	def test_no_project_so_add_Project(self):



		self.browser.get(self.live_server_url)


		add_url = self.live_server_url + reverse('add')
		self.browser.find_element_by_tag_name('a').click()
		self.assertEquals(self.browser.current_url , add_url)



	def test_project_list_vies_user(self):
		project1 = Project.objects.create(
			name = 'project1',
			budget = 10000
		)



		self.browser.get(self.live_server_url)

		self.assertEquals(  self.browser.find_element_by_tag_name('h5').text , 'project1' )




	def test_user_ubdget_exists(self):

		project1 = Project.objects.create(
			name = 'project1',
			budget = 10000
		)



		self.browser.get(self.live_server_url)


		detail_url = self.live_server_url + reverse('detail' , args=[project1.slug])
		self.browser.find_element_by_link_text('VISIT').click()
		self.assertEquals(self.browser.current_url , detail_url)
















