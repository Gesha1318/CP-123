from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Role, SectionMembership


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
	list_display = ("name", "description", "created_at")
	search_fields = ("name", "description")
	list_filter = ("created_at",)
	ordering = ("name",)
	
	# Use custom templates for beautiful styling
	change_form_template = "admin/custom_form.html"
	change_list_template = "admin/custom_change_list.html"


class SectionMembershipInline(admin.TabularInline):
	model = SectionMembership
	extra = 0
	autocomplete_fields = ("section", "role")
	fields = ("section", "permission", "role")


@admin.register(SectionMembership)
class SectionMembershipAdmin(admin.ModelAdmin):
	list_display = ("user", "section", "role", "joined_at")
	list_filter = ("section", "role", "joined_at")
	search_fields = ("user__username", "section__name", "role__name")
	ordering = ("-joined_at",)
	
	# Use custom templates for beautiful styling
	change_form_template = "admin/custom_form.html"
	change_list_template = "admin/custom_change_list.html"


# Attach inline to User admin for quick permission editing
User = get_user_model()
try:
	from django.contrib.auth.admin import UserAdmin
	admin.site.unregister(User)
	@admin.register(User)
	class CustomUserAdmin(UserAdmin):
		inlines = [SectionMembershipInline]
except admin.sites.NotRegistered:
	pass
