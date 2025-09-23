from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Role, SectionMembership



@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
	list_display = ("name", "description")
	search_fields = ("name", "description")
	ordering = ("name",)
	save_on_top = True
	list_per_page = 25
	
	# Use specific custom templates for beautiful styling
	change_form_template = "admin/accounts/role/change_form.html"
	change_list_template = "admin/custom_change_list.html"


class SectionMembershipInline(admin.TabularInline):
	model = SectionMembership
	extra = 1
	autocomplete_fields = ("section", "role")
	fields = ("section", "permission", "role")



@admin.register(SectionMembership)
class SectionMembershipAdmin(admin.ModelAdmin):
	list_display = ("user", "section", "role", "created_at")
	list_filter = ("section", "role", "created_at")
	search_fields = ("user__username", "section__name", "role__name")
	ordering = ("-created_at",)
	date_hierarchy = "created_at"
	save_on_top = True
	list_per_page = 25
	
	# Use specific custom templates for beautiful styling
	change_form_template = "admin/accounts/sectionmembership/change_form.html"
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
