from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import TemplateView
from classBasedView.views import classBased, MyView,\
    ClassDetailView, ClassListView, ClassCreateView, \
    ClassUpdateView, ClassDeleteView


urlpatterns = [
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/', 'newsletter.views.contact', name='contact'),
    url(r'^about/', 'tryDjango.views.about', name='about_name'),
    url(r'^frontend/', 'newsletter.views.frontend', name='frontend'),
    url(r'^classView/', TemplateView.as_view(template_name="classBasedView/classBasedMain.html") ,name="classView"),
    url(r'^classTemplateViewAbout/',  classBased.as_view() ,name="classTemplateViewAbout"),
    url(r'^classBaseViewAbout/',  MyView.as_view(template_name ="classBasedView/BaseView.html") ,name="classBaseViewAbout"),
    url(r'^class/create/$',  ClassCreateView.as_view() ,name="class_create"),
    url(r'^class/(?P<slug>[-\w]+)/$',  ClassDetailView.as_view() ,name="class_detail"),
    url(r'^class/(?P<slug>[-\w]+)/delete/$',  ClassDeleteView.as_view() ,name="class_delete"),
    url(r'^class/(?P<slug>[-\w]+)/update/$',  ClassUpdateView.as_view() ,name="class_update"),
    url(r'^class/$',  ClassListView.as_view() ,name="class_list"),
    url(r'^accounts/', include('registration.backends.default.urls'))

    #url(r'^accounts/', include('registration.backends.default.urls')),
]

#Here we are appending static urls with url patterns
# we are using settings.Debug here so that we should keep in mind that on production we should Debug : False

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)