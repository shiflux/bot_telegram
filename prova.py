from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultPhoto
from telegram.ext import InlineQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(token='291112291:AAEvjVVIaIXJU5YdbQUwIOuaoJ6517Oiqw4')
dispatcher = updater.dispatcher

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

echo_handler = MessageHandler([Filters.text], echo)
dispatcher.add_handler(echo_handler)


# def caps(bot, update, args):
#     text_caps = ' '.join(args).upper()
#     bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)
#
# caps_handler = CommandHandler('caps', caps, pass_args=True)
# dispatcher.add_handler(caps_handler)

def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    # results.append(
    #     InlineQueryResultPhoto(
    #         id="6",
    #         photo_url='http://digilander.libero.it/principe69_9/cane.jpg',
    #         thumb_url='http://digilander.libero.it/principe69_9/cane.jpg')
    # )
    # results.append(
    #     InlineQueryResultPhoto(
    #         id="14",
    #         photo_url='https://www.nrdc.org/sites/default/files/import/switchboard/blogs/pdelforge/assets_c/2012/09/Desktop_PC_web_small-thumb-448x336-8008.jpg',
    #         thumb_url='https://www.nrdc.org/sites/default/files/import/switchboard/blogs/pdelforge/assets_c/2012/09/Desktop_PC_web_small-thumb-448x336-8008.jpg')
    # )
    # results.append(
    #     InlineQueryResultArticle(
    #         id = query.upper(),
    #         title = 'Caps',
    #         input_message_content = InputTextMessageContent(query.upper())
    #     )
    # )
    bot.answerInlineQuery(update.inline_query.id, results)


inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

updater.start_polling()