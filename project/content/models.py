from django.db import models
from library.models import BaseModel
from library.models import NamedModel
from project.library.models import OrderedNamedModel


class SiteSettings(BaseModel):
    """
    General settings
    """
    default_title   = models.CharField(max_length=50, null=True, blank=True)
    heading         = models.CharField(max_length=50, null=True, blank=True)
    description     = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.default_title

    
class Page(NamedModel):
    """
    A page on the site
    """
    heading             = models.CharField(max_length=50, help_text='defaults to name if not present', null=True, blank=True)
    content             = models.TextField(null=True, blank=True)

    class Meta: