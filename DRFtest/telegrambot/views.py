from multiprocessing import Process
from time import sleep

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


from rest_framework.decorators import action, api_view
from rest_framework import renderers

from .BusinessLogic.GoogleDriveService import GoogleDriveService
from .Core.GoogleDriveServiceInterface import GoogleDriveServiceItnerface
from .BusinessLogic.TelegramBotService import TelegramBotService

@api_view()
def loadfiledb(request, *args, **kwargs):
    google_service: GoogleDriveServiceItnerface  = GoogleDriveService()
    google_service.syncDb()
    return Response('ok')

@api_view()
def starttelegrambot(request, *args, **kwargs):
    telegram_service = TelegramBotService()
    result = telegram_service.start()
    return Response(f'Operation start returned status: {result}')


@api_view()
def stoptelegrambot(request, *args, **kwargs):
    telegram_service = TelegramBotService()
    result = telegram_service.stop()
    return Response(f'Operation stop returned status: {result}')

@api_view()
def statustelegrambot(request, *args, **kwargs):
    telegram_service = TelegramBotService()
    result = telegram_service.status()
    return Response(f'Operation status returned status: {result}')