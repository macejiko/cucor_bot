#!/usr/bin/env python3

import logging
import random

from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import (
    Updater,
    InlineQueryHandler,
    MessageHandler,
    Filters,
)


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)
logger = logging.getLogger(__name__)


updater = Updater(token="XXXXXXXXXXXXXXXXXXXXXXXXX", use_context=True)
dispatcher = updater.dispatcher


def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=random.randint(0, 99999999),
            title="Caps",
            input_message_content=InputTextMessageContent("123"),
        )
    )
    results.append(
        InlineQueryResultArticle(
            id=random.randint(0, 99999999),
            title="log",
            input_message_content=InputTextMessageContent("AAA"),
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)


def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Use only inline mode!"
    )


inline_caps_handler = InlineQueryHandler(inline_caps)
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(inline_caps_handler)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()
