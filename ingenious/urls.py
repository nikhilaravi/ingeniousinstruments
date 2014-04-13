from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from ingenious import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ingenious.views.home', name='home'),
    # url(r'^ingenious/', include('ingenious.foo.urls')),

    url(r'^$', 'ingenious.views.home'),
    url(r'^about/', 'ingenious.views.about'),
    url(r'^upload/', 'ingenious.views.upload'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
