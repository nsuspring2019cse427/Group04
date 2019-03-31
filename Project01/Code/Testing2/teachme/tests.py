# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
from django.test import TestCase

from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse
from .models import teachers , StudentPost
from . import views


class HomePageTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/teachme/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/teachme/')
        self.assertContains(response, '<h1>শিক্ষক দিচ্ছি-নিচ্ছি!</h1>')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/teachme/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')


    

            
            
     
   



class tryTest(TestCase):


    def test_add(self):
        result = views.add(10 ,5)
        self.assertEquals(result , 15)
        

    def test_not_right(self):
        
        self.assertNotEqual(views.add(12 , 1) ,14)
               



    
    

    def test_home_page_status_code(self):
        response = self.client.get('/teachme/createPost/')
        self.assertEquals(response.status_code, 200)

       
    
    def test_home_page_status_code(self):
        response = self.client.get('/somethingThatIsFalse/createPost/')
        self.assertEquals(response.status_code, 404)
    
    
    
    def test_home_page_status_code(self):
        response = self.client.get('/somethingThatIsFalse/createPost/')
        self.assertNotEqual(response.status_code, 200)
    
    
    
    
    
    
    
    
    def test_Passing_name_value_url(self):
        response = self.client.get('/teachme/student_profile/t_list/')
        self.assertEqual(response.status_code , 200)

    def test_logout(self):
        response = self.client.get('/teachme/profile/logout/')
        self.assertEqual(response.status_code , 302)
    
    def test_user_in_database(self):

        teachers.objects.create(Tname="della"  )
        self.assertEqual(teachers.objects.get(Tname="della").Tname , "della")
        
        
        
        
class using_coverage(TestCase):
    
    
    
    def test_home_page_status_code(self):
        response = self.client.get('/teachme/')
        self.assertEquals(response.status_code, 200)
        
        
    def test_home_page_to_Teachers_login(self):
        response = self.client.get('/teachme/signin/')
        self.assertEquals(response.status_code, 200)
        
        
        
        
    
    
    

      
        
        
        
        
    
     





  
   
        
    
    

    
    
