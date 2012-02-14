from django.conf import settings as _settings
from project.content.models import SiteSettings
import constants


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
        'constants': constants,
        'MEDIA_URL': _settings.MEDIA_URL,
        'STATIC_URL': _settings.STATIC_URL,
        'site': site_settings,
    }

