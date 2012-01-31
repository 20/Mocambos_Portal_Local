from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# For Django-Filer
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

## For Django-Filebrowser >= 3.4.0
from filebrowser.sites import site

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Mocambos_Portal.views.home', name='home'),
    # url(r'^Mocambos_Portal/', include('Mocambos_Portal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
#    # For Django-Grappelli
    url(r'^grappelli/', include('grappelli.urls')),
    ## For Django-Filebrowser 3.4.0
    url(r'^admin/filebrowser/', include(site.urls)),
#    # For Django-Filebrowser 3.3.0
#    url(r'^admin/filebrowser/', include('filebrowser.urls')),
    # For django_bfm
    url(r'^files/', include('django_bfm.urls')),
)

# For Django-Filer
#urlpatterns += staticfiles_urlpatterns()

# Let Django serve media files in Debug Mode
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
