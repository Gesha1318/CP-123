from django.contrib.auth import get_user_model
from sections.models import Section
from documents.models import Article, File

def admin_stats(request):
    """
    Context processor to add statistics for admin dashboard
    """
    if request.path.startswith('/admin/'):
        try:
            User = get_user_model()
            return {
                'user_count': User.objects.count(),
                'section_count': Section.objects.count(),
                'article_count': Article.objects.count(),
                'file_count': File.objects.count(),
            }
        except Exception:
            # Return default values if database is not ready
            return {
                'user_count': 0,
                'section_count': 0,
                'article_count': 0,
                'file_count': 0,
            }
    return {}