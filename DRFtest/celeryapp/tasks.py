# Create your tasks here
import random
import string
from time import sleep

from celery import shared_task
from .models import CeleryModel


@shared_task
def create_new_object():
    sleep(5)
    random_name = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
    new_object = CeleryModel.objects.create(name=random_name)
    return new_object.name


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)