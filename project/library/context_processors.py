from django.conf import settings as _settings
from project.content.models import SiteSettings


def settings(request):
    """
    General settings
    """
    try:
        site_settings = SiteSettings.objects.all()[0]
    except IndexError:
        site_settings = None

    return {
        'settings': _settings,
#        'STATIC_URL': _settings.STATIC_URL,
        'site': site_settings,
    }

