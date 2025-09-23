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

# Remove duplicate registrations; apps handle their own admin registrations