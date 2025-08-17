from django.urls import path
from . import views


urlpatterns = [
	path('<slug:section_slug>/articles/new/', views.create_article, name='create_article'),
	path('<slug:section_slug>/articles/<slug:article_slug>/', views.article_detail, name='article_detail'),
	path('<slug:section_slug>/files/upload/', views.upload_file, name='upload_file'),
]