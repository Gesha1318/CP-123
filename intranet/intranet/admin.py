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

# Register models with default admin site
from accounts.models import Role, SectionMembership
from sections.models import Section
from documents.models import Article, File

# Import admin classes
from accounts.admin import RoleAdmin, SectionMembershipAdmin
from sections.admin import SectionAdmin
from documents.admin import ArticleAdmin, FileAdmin

# Register with default admin site
admin.site.register(Role, RoleAdmin)
admin.site.register(SectionMembership, SectionMembershipAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(File, FileAdmin)