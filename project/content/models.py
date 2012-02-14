from django.db import models
from library.models import BaseModel, OrderedContentModel


class SiteSettings(BaseModel):
    """
    General settings
    """
    default_title   = models.CharField(max_length=50, null=True, blank=True)
    heading         = models.CharField(max_length=50, null=True, blank=True)
    description     = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.default_title


class Page(OrderedContentModel):
    """
    A page on the site
    """
    heading             = models.CharField(max_length=50, help_text='defaults to title if not present', null=True, blank=True)
    content             = models.TextField(null=True, blank=True)

