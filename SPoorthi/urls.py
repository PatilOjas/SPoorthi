"""SPoorthi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings

from django.urls import include, re_path
from django.views.static import serve


urlpatterns = [
    path('8a2hn879f7ui4ha0/', admin.site.urls, name="admin"),
	path('registration/<str:name>', views.registrationPage, name="registrationpage"),
	path('', views.homePage, name='homepage'),
	path('gallery/', views.gallery, name="gallery"),
	path('events/', views.eventPage, name="events"),
	path('events/<str:name>/', views.eventPage, name="event_details"),
    path('contactUs/', views.contact, name='contact'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)