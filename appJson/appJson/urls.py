from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'appJson.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('appJson.apps.home.urls')),
    url(r'^ws/',include('appJson.apps.WEBservices.wsProductos.urls')),

)
