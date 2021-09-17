
import time
from datetime import datetime
from os import getenv
from typing import Any

import pytz
from dotenv import load_dotenv

load_dotenv()


var1 = getenv('QWERTY1')
print(var1)

timestamp = str(round(time.time(), 3)).replace('.','')
print(timestamp)

local_date = datetime.now(pytz.timezone('Asia/Yekaterinburg'))

timestamp = str(round(time.time(), 3)).replace('.','')
print(timestamp)


class Realisation():
    _somevalue: str

    def __init__(self):
        self._somevalue = '123454321'

    def method(self, value: str):
        self._hidden_logic_method()

    def _hidden_logic_method(self):
        print(self._somevalue)


class Interface(Realisation):

    def method(self, *args, **kwargs):
        super().method(*args, **kwargs)

test1 = Interface()
test1.method('11111')