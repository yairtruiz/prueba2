from django.shortcuts import render
from django.http import HttpResponse
from appJson.apps.home.models import Articulos
from django.core import serializers

def wsProductos_view(request):
	data = serializers.serialize("xml",Articulos.objects.all())
	#retorna la informaci'on en formato json
	return  HttpResponse(data,content_type='application/xml')
