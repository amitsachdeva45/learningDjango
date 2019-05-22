from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/', 'newsletter.views.contact', name='contact'),
    url(r'^about/', 'tryDjango.views.about', name='about_name'),
    url(r'^frontend/', 'newsletter.views.frontend', name='frontend'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^classView/', include(admin.site.urls)),
    #url(r'^accounts/', include('registration.backends.default.urls')),
]

#Here we are appending static urls with url patterns
# we are using settings.Debug here so that we should keep in mind that on production we should Debug : False

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)