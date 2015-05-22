from django.conf.urls import url, patterns
from .views import wsProductos_view

urlpatterns = patterns('',
		

		url(r'^productos/$',wsProductos_view, name='ws_producto'),


)