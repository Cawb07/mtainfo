mtainfo
=======

Web App for checking MTA Services' Statuses'

To add this app to any Django project, make appropriate changes in the project's settings.py and urls.py.

In settings.py, add to:

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # Uncomment the next line to enable the admin:
        'django.contrib.admin',
        # Uncomment the next line to enable admin documentation:
        # 'django.contrib.admindocs',
        'mtainfo',
)

In urls.py, add to:

    urlpatterns = patterns('',
        # Uncomment the next line to enable the admin:
        url(r'^mtainfo/', include('mtainfo.urls')),
        url(r'^admin/', include(admin.site.urls)),
    )
