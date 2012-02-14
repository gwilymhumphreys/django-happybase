from django.db import models
from decimal import Decimal

class CurrencyField(models.DecimalField):
    __metaclass__ = models.SubfieldBase

    def to_python(self, value):
        try:
            return super(CurrencyField, self).to_python(value).quantize(Decimal('0.01'))
        except AttributeError:
            return None

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^library\.fields\.CurrencyField"])
except:
    pass
