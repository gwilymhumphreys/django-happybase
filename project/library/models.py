from django.db import models


class BaseModel(models.Model):
    """
    Basic model
    """
    created     = models.DateTimeField(auto_now_add=True, editable=False)
    modified    = models.DateTimeField(auto_now=True, editable=False)
    modified    = models.DateTimeField(auto_now=True, editable=False)
    visible     = models.BooleanField(default=True)

    class Meta:
        abstract = True


class NamedModel(BaseModel):
    """
    Basic model with a title and slug
    """
    title           = models.CharField(max_length=50)
    slug            = models.SlugField(max_length=50)

    class Meta:
        abstract = True
        ordering = ('title', )

    def __unicode__(self):
        return self.title


class OrderedNamedModel(NamedModel):
    """
    Named model with an ordering field
    """
    order           = models.PositiveIntegerField(null=True, blank=True, )

    class Meta:
        abstract = True
        get_latest_by = 'order'
        ordering = ('order', )
