from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Role, SectionMembership


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
	list_display = ("name", "description")
	search_fields = ("name",)


class SectionMembershipInline(admin.TabularInline):
	model = SectionMembership
	extra = 0
	autocomplete_fields = ("section", "role")
	fields = ("section", "permission", "role")


@admin.register(SectionMembership)
class SectionMembershipAdmin(admin.ModelAdmin):
	list_display = ("user", "section", "permission", "role", "created_at")
	list_filter = ("permission", "section")
	search_fields = ("user__username", "section__name")
	autocomplete_fields = ("user", "section", "role")


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
