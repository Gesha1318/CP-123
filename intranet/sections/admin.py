from django.contrib import admin
from .models import Section, SectionMembership


class SectionMembershipInline(admin.TabularInline):
    model = SectionMembership
    extra = 1


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent', 'is_private', 'created_at')
    list_filter = ('is_private', 'created_at')
    search_fields = ('name', 'slug', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [SectionMembershipInline]


@admin.register(SectionMembership)
class SectionMembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'section', 'role', 'date_joined')
    list_filter = ('role', 'date_joined')
    search_fields = ('user__username', 'section__name')


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
	list_filter = ("is_private",)
	ordering = ("name",)
	save_on_top = True
	list_per_page = 25
	
	# Use specific custom templates for beautiful styling
	change_form_template = "admin/sections/section/change_form.html"
	change_list_template = "admin/custom_change_list.html"
