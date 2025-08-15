from django.contrib import admin
from .models import Article, File


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ("title", "section", "is_published", "created_at")
	list_filter = ("section", "is_published")
	search_fields = ("title", "slug", "content")
	prepopulated_fields = {"slug": ("title",)}
	autocomplete_fields = ("section", "author")
	fieldsets = (
		(None, {"fields": ("section", "title", "slug", "is_published")}),
		("Содержимое", {"fields": ("content",)}),
		("Автор", {"fields": ("author",)}),
	)


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
	list_display = ("title", "section", "created_at")
	list_filter = ("section",)
	search_fields = ("title",)
	autocomplete_fields = ("section", "uploaded_by")
	fields = ("section", "title", "file", "uploaded_by")
