from django.contrib import admin
from .models import Article, File


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ("title", "section", "author", "is_published", "created_at")
	list_filter = ("section", "is_published", "created_at", "author")
	search_fields = ("title", "content", "section__name", "author__username")
	prepopulated_fields = {"slug": ("title",)}
	ordering = ("-created_at",)
	date_hierarchy = "created_at"
	save_on_top = True
	list_per_page = 25
	
	# Use specific custom templates for beautiful styling
	change_form_template = "admin/documents/article/change_form.html"
	change_list_template = "admin/custom_change_list.html"


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
	list_display = ("title", "section", "file", "created_at")
	list_filter = ("created_at", "section")
	search_fields = ("title", "section__name")
	ordering = ("-created_at",)
	date_hierarchy = "created_at"
	save_on_top = True
	list_per_page = 25
	
	# Use specific custom templates for beautiful styling
	change_form_template = "admin/documents/file/change_form.html"
	change_list_template = "admin/custom_change_list.html"
