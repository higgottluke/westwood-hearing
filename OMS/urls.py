from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
	url(r'^patients/$', views.patient_list, name='patient-list'),
	url(r'^patient/(?P<id>\d+)/$', views.patient_profile, name='patient-info'),
	url(r'^patient/new/$', views.newpatient, name='new-patient'),
	url(r'^calendar/$', views.calendar, name='appointment-calendar'),
	url(r'^audiogram/(?P<id>\d+)/$', views.audiogram, name='audiogram'),
]
