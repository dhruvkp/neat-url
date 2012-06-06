from django.conf.urls import patterns, include, url
from app.views import home,keywords,redirect
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('app.views',
    # Examples:
    url(r'^$', 'home'),
    url(r'^keywords$', 'keywords'),
    url(r'^(?P<tocken>[^/]+)','redirect'),
    # url(r'^url/', include('url.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
