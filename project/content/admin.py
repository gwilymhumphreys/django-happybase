from django.db.models import get_models
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from library.admin import NamedModelAdmin, NamedModelInline
from models import *


import models
for model in get_models(models):
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
