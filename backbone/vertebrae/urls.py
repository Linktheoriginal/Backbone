from django.conf.urls import url
from django.conf.urls import include

from . import views

from vertebrae.viewsets import *
from rest_framework import routers

routerc3 = routers.DefaultRouter()
routerc3.register(r'todo', ToDoItemViewSet)

routerc4 = routers.DefaultRouter()
routerc4.register(r'products', ProductViewSet)

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^c1/', views.c1, name='c1'),
	url(r'^c2/', views.c2, name='c2'),
	url(r'^c3/', views.c3, name='c3'),
	url(r'^c3api/', include(routerc3.urls)),
	url(r'^c4/', views.c4, name='c4'),
	url(r'^c4api/', include(routerc4.urls)),
	url(r'^c5/', views.c5, name='c5'),
	url(r'^c6/', views.c6, name='c6'),
	url(r'^c7/', views.c7, name='c7'),
	url(r'^c8/', views.c8, name='c8'),
]