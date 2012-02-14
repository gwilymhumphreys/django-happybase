from django.contrib import admin
from django.conf import settings


class TinymceMixin():
    class Media:
        js = [
            '%s/tinymce/jscripts/tiny_mce/tiny_mce.js' % settings.ADMIN_MEDIA_PREFIX,
            '%s/tinymce_setup/tinymce_setup.js' % settings.ADMIN_MEDIA_PREFIX,
        ]

class NamedModelAdmin(admin.ModelAdmin, TinymceMixin):
    prepopulated_fields = {'slug': ('title',)}


class NamedModelInline(admin.TabularInline):
    prepopulated_fields = {'slug': ('title',)}
