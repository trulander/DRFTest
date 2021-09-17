# Create your tasks here
import random
import string
from time import sleep

import telegram
from celery import shared_task
from telegram.ext import CallbackContext


@shared_task
def send_message():
    pass