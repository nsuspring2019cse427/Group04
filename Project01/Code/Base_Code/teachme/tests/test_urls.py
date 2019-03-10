#!/usr/bin/python

#!/usr/bin/python

from django.test import SimpleTestCase
from django.urls import reverse , resolve
from teachme.views import project_list , project_detail ,  ProjectCreateView



class TestUrls(SimpleTestCase):



	def test_list_urls_is_resolved(self):


		url = reverse('list')
		print(resolve(url))
		self.assertEquals(resolve(url).func, project_list)




	def test_add_urls_is_resolved(self):


			url = reverse('add')
			print(resolve(url))
			self.assertEquals(resolve(url).func.view_class, ProjectCreateView)




	
