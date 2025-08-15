from django.urls import path
from . import views


urlpatterns = [
	path('', views.section_list, name='section_list'),
	path('new/', views.section_create, name='section_create'),
	path('<slug:slug>/', views.section_detail, name='section_detail'),
	path('<slug:slug>/edit/', views.section_edit, name='section_edit'),
	path('<slug:slug>/members/', views.section_members, name='section_members'),
]