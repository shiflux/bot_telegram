from bot import base_bot
from telegram.ext import MessageHandler, Filters, CommandHandler, InlineQueryHandler
from telegram import InlineQueryResultPhoto
from utils import *
from sett import settings

b = base_bot(token=settings.token)


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Write @bot to get images!")

start_handler = CommandHandler('start', start)
b.add_command(start_handler)

data_images = get_from_json(settings.server+settings.setup_json, "images")
images_dict = {}
for x in range(len(data_images)):
    images_dict[data_images[x]["name"]] = (data_images[x]["link"],data_images[x]["thumbnail"])


def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    queries = query.split()
    results = list()
    matching = [s for s in images_dict if all(item in s for item in queries)]
    for x in range(len(matching)):
        results.append(
            InlineQueryResultPhoto(
                id=matching[x],
                photo_url=images_dict[matching[x]][0],
                thumb_url=images_dict[matching[x]][1])
        )

    bot.answerInlineQuery(update.inline_query.id, results)

inline_caps_handler = InlineQueryHandler(inline_caps)
b.add_command(inline_caps_handler)

b.run()