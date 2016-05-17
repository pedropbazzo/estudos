"""gerenciador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
import django
from agenda import views


urlpatterns = [
    url(r'^admin/', admin.site.urls, name='index'),
    url(r'^$', views.lista, name='lista'),
    url(r'^adiciona/$', views.adiciona, name='adiciona'),
    url(r'^remove/(?P<id_item>\d+)/$', views.remove, name='remove'),
    url(r'^item/(?P<id_item>\d+)/$', views.item, name='item'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', django.views.static.serve,
            {'document_root': settings.MEDIA_URL}),
    ]
