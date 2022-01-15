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

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
	# path('registration/', views.registrationPage, name="registrationpage"),
	path('registration/<str:name>', views.registrationPage, name="registrationpage"),
	path('', views.homePage, name='homepage'),
	path('gallery/', views.gallery, name="gallery"),
	path('events/', views.eventPage, name="events"),
	path('events/<str:name>/', views.eventPage, name="event_details"),
    path('contactUs/', views.contact, name='contact'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)