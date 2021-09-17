import os
from multiprocessing import Process, Lock
from time import sleep

import logging
import telegram
from telegram import InlineQueryResultArticle, InputTextMessageContent

from telegram.ext import Updater, Dispatcher, CallbackContext, InlineQueryHandler
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

from ..tasks import *

class TelegramBotService(object):
    _proc: Process = None
    _api_key = '-'

    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super(TelegramBotService, cls).__new__(cls)
        #print(id(cls))
        return cls._instance


    def start(self) -> bool:
        if not self._proc or not self._proc.is_alive():
            self._proc = Process(target=self._process_loop, name='telegrambot')
            self._proc.start()
            return True
        return False


    def stop(self) -> bool:
        self._proc.terminate()
        return True


    def status(self) -> bool:
        return self._proc.is_alive()


    #@classmethod
    def _process_loop(self):
        updater = Updater(token=self._api_key)
        dispatcher: Dispatcher = updater.dispatcher

        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

        def start(update, context: telegram.ext.CallbackContext):
            context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

        start_handler = CommandHandler('start', start)
        dispatcher.add_handler(start_handler)

        def echo(update, context: CallbackContext):
            context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

        echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
        dispatcher.add_handler(echo_handler)

        def caps(update, context):
            text_caps = ' '.join(context.args).upper()
            context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

        caps_handler = CommandHandler('caps', caps)
        dispatcher.add_handler(caps_handler)

        def inline_caps(update, context):
            query = update.inline_query.query
            if not query:
                return
            results = list()
            results.append(
                InlineQueryResultArticle(
                    id=query.upper(),
                    title='Caps',
                    input_message_content=InputTextMessageContent(query.upper())
                )
            )
            context.bot.answer_inline_query(update.inline_query.id, results)

        inline_caps_handler = InlineQueryHandler(inline_caps)
        dispatcher.add_handler(inline_caps_handler)

        def unknown(update, context):
            context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

        unknown_handler = MessageHandler(Filters.command, unknown)
        dispatcher.add_handler(unknown_handler)

        updater.start_polling()

        updater.idle()
        #updater.stop()
        # while True:
        #     sleep(5)
        #     print(f'passed 5 second {os.getpid()}')