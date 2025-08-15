from django.contrib import admin
from .models import Section


class ChildSectionInline(admin.TabularInline):
	model = Section
	extra = 0
	fk_name = 'parent'
	fields = ("name", "slug", "is_private")
	show_change_link = True


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
	list_display = ("name", "parent", "is_private")
	search_fields = ("name", "slug")
	prepopulated_fields = {"slug": ("name",)}
	inlines = [ChildSectionInline]
