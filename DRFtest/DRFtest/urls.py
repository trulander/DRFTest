"""DRFtest URL Configuration

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

from rest_framework import routers
from django.conf.urls import url, include
from django.urls import path

from rest_framework.schemas import get_schema_view

import quickstart.views as quickstart_view
import snippets.views as snippets_view

router = routers.DefaultRouter()

router.register(r'quickstart_users', quickstart_view.UserViewSet)
router.register(r'quickstart_groups', quickstart_view.GroupViewSet)

router.register(r'snippets', snippets_view.SnippetViewSet)
router.register(r'users', snippets_view.UserViewSet)

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url(r'^', include(router.urls)),
    #url(r'^', include('snippets.urls')),
    path('telegramapi/', include('telegrambot.urls')),
    path('celery/', include('celeryapp.urls')),
    path('schema/', schema_view),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     path('admin/', admin.site.urls),
# ]
