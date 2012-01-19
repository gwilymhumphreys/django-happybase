from django.db import models


class BaseModel(models.Model):
    created     = models.DateTimeField(auto_now_add=True, editable=False)
    modified    = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class NamedModel(BaseModel):
    name            = models.CharField(max_length=50)
    slug            = models.SlugField(max_length=50)

    class Meta:
        abstract = True
        ordering = ('name', )

    def __unicode__(self):
        return self.name

    def _get_isotope_tag(self):
        return '%s' % self.slug
    isotope_tag = property(_get_isotope_tag)


class OrderedNamedModel(NamedModel):

    order           = models.IntegerField(null=True, blank=True, )

    class Meta:
        abstract = True
        get_latest_by = 'order'
        ordering = ('order', )
