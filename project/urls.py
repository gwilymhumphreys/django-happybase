from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
)

urlpatterns += patterns('content.views',
    url(r'^$', 'home', name='home'),
    url(r'^(?P<slug>[^/]+)/$', 'page', name='page'),
)


# To serve media while in development
if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
        url(r'^static-media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': getattr(settings, 'STATICFILES_ROOT', ''), 'show_indexes': True}),
    )
