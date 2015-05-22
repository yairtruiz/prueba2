from django.conf.urls import url, patterns
from .views import Index_view

urlpatterns =patterns('',
		

		url(r'^$', Index_view.as_view(), name='ws_Productos'),
		

)