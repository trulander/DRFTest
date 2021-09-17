from django.conf.urls import url
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from .views import *

# router = routers.DefaultRouter()
# router.register(r'telegrambotapi', GoogleDriveView)



urlpatterns = [
    path('loadfile/', loadfiledb, name='googledriveview'),
    path('startbot/', starttelegrambot, name='startbot'),
    path('stopbot/', stoptelegrambot, name='stopbot'),
    path('statusbot/', statustelegrambot, name='statusbot')
]