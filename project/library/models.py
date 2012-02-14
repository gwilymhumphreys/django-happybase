from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext as _


class BaseModel(models.Model):
    """
    Basic model
    """
    created         = models.DateTimeField(_('Created'), auto_now_add=True, editable=False)
    modified        = models.DateTimeField(_('Modified'), auto_now=True, editable=False)

    class Meta:
        abstract = True


class SiteSettings(BaseModel):
    """
    General site settings
    """
    title           = models.CharField(max_length=50)
    heading         = models.CharField(max_length=50)
    description     = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class NamedModel(BaseModel):
    """
    Basic model with a name and slug
    """
    name            = models.CharField(_('Name'), max_length=200)
    slug            = models.SlugField(_('Slug'), max_length=200)

    class Meta:
        abstract = True
        ordering = ('name', )

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(NamedModel, self).save(*args, **kwargs)


class OrderedNamedModel(NamedModel):
    """
    Named model with an ordering field
    """
    order           = models.PositiveIntegerField(_('Order'), default=0)

    class Meta:
        abstract = True
        get_latest_by = 'order'
        ordering = ('order', )


class ContentModel(BaseModel):
    """
    Basic model with a title, slug and content
    """
    title           = models.CharField(_('Title'), max_length=200)
    slug            = models.SlugField(_('Slug'), max_length=200)
    visible         = models.BooleanField(_('Visible'))
    content         = models.TextField(_('Content'), null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ('title', )

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(ContentModel, self).save(*args, **kwargs)


class OrderedContentModel(ContentModel):
    """
    Content model with an ordering field
    """
    order           = models.PositiveIntegerField(_('Order'), default=0)

    class Meta:
        abstract = True
        get_latest_by = 'order'
        ordering = ('order', )
