#!/usr/bin/python

#!/usr/bin/python

from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django import forms
from rest_framework.urlpatterns import format_suffix_patterns





urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^post/$',views.post),
	url(r'^signin/$',views.signin),
	url(r'^student_signin/$',views.student_signin),
	url(r'^signup/$',views.signup),
	url(r'^student_signup/$',views.student_signup),
	
	url(r'^student_profile/$',views.student_profile),
	url(r'^student_profile/t_list/$',views.t_list),
	url(r'^student_profile/logout/$',views.logout),
	url(r'^student_profile/logout/$',views.logout),
	url(r'^student_profile/createPost/$',views.createPost),
	url(r'^student_profile/t_list/(.*)/$',views.test1), # this is my special tricks 
	
	url(r'^profile/$',views.profile),
	url(r'^profile/logout/$',views.logout),
	url(r'^info/$',views.info),
	url(r'^signin/s_login/$',views.s_login),
	url(r'^student_signin/s_login/$',views.s_login),


	url(r'^s_home/$',views.s_home),
	url(r'^s_home/profile/$',views.back_profile),
	url(r'^set_profile$',views.set_profile),
	url(r'^set_student_profile$',views.set_student_profile),
	url(r'^profile/t_list',views.t_list),
	url(r'^profile/studentPostList/', views.studentPostList),
	url(r'^profile/(.*)/$',views.test1),
	url(r'^singupprocess',views.singupprocess),
	url(r'^student_singupprocess',views.student_singupprocess),
	url(r'^search',views.search),
	url(r'^searchprocess',views.searchprocess),
	url(r'^createPost/$',views.createPost),
	url(r'^student_profile/createPost/createPostProcess',views.createPostProcess ),
	url(r'^stocks/$',views.TeachersList.as_view()),
	url(r'^rest_students/$',views.StudentsList.as_view()),
	
	
	
	
	
	url(r'^auth/', include('social_django.urls', namespace='social')),
	
	
	
	
]


urlpatterns += staticfiles_urlpatterns()





urlpatterns = format_suffix_patterns(urlpatterns)


