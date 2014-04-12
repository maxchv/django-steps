from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', TemplateView.as_view(template_name="index.html"), name='home'),
    url(r'^complaints$', "complaints.views.index", name="complaints_index"),
    url(r'^admin/', include(admin.site.urls)),

)
