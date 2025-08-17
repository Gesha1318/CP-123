from django.contrib import admin
from django.contrib.auth.models import Group

# Hide Django Groups from admin
try:
    admin.site.unregister(Group)
except admin.sites.NotRegistered:
    pass

# Hide Allauth Social models if present
try:
    from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken
    for _model in (SocialAccount, SocialApp, SocialToken):
        try:
            admin.site.unregister(_model)
        except admin.sites.NotRegistered:
            pass
except Exception:
    pass

# Customize admin site
admin.site.site_header = "Интранет - Администрирование"
admin.site.site_title = "Интранет"
admin.site.index_title = "Добро пожаловать в панель управления Интранет"

# Custom admin site class
class CustomAdminSite(admin.AdminSite):
    change_form_template = 'admin/custom_form.html'
    change_list_template = 'admin/custom_change_list.html'
    
    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        app_dict = self._registry._registry
        
        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
        
        # Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: x['name'])
        
        return app_list

# Create custom admin site instance
custom_admin_site = CustomAdminSite(name='custom_admin')

# Register models with custom admin site
from accounts.models import Role, SectionMembership
from sections.models import Section
from documents.models import Article, File

# Register with custom admin site
custom_admin_site.register(Role)
custom_admin_site.register(SectionMembership)
custom_admin_site.register(Section)
custom_admin_site.register(Article)
custom_admin_site.register(File)

# Also register with default admin site for compatibility
from accounts.admin import RoleAdmin, SectionMembershipAdmin
from sections.admin import SectionAdmin
from documents.admin import ArticleAdmin, FileAdmin

admin.site.register(Role, RoleAdmin)
admin.site.register(SectionMembership, SectionMembershipAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(File, FileAdmin)