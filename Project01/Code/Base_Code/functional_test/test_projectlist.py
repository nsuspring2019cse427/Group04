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

