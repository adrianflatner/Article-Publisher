"""Scrumfeed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from Scrumfeed import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #Everything that starts with "ScrummerTimes" is going to be passed out to the ScrummerTimes/url
    url(r'^$', include('ScrummerTimes.urls')),
    path('ScrummerTimes/', include('ScrummerTimes.urls')),
    url(r'^accounts/', include('accounts.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#Static is used to handle things like media

urlpatterns += staticfiles_urlpatterns()