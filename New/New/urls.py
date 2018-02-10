
from django.conf.urls import url, include
from django.contrib import admin
from oscar.app import application

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(application.urls)),
    url(r'^auth/', include('allauth.urls')),
    url(r'^app/', include('petzoapp.urls')),
]
