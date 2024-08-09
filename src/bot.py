import logging.config
from pathlib import Path

from telethon import TelegramClient, events

import logging_setup
from config_reader import config

logging_config = logging_setup.get_logging_config("resenderbot")
logging.config.dictConfig(logging_config)


def main():
    Path("logs").mkdir(exist_ok=True)
    with TelegramClient('resender', config.API_ID, config.API_HASH) as client:
        @client.on(events.NewMessage(outgoing=False))
        async def handler(event: events.NewMessage.Event):
            if event.chat_id == config.GROUP_ID and event.message.text:
                await client.send_message(config.ADMIN_ID, event.message.text)
                logging.info(event.message)

        @client.on(events.MessageEdited(outgoing=False))
        async def handler(event: events.MessageEdited.Event):
            if event.chat_id == config.GROUP_ID and event.message.text:
                await client.send_message(config.ADMIN_ID, "EDITED: " + event.message.text)
                logging.info(event.message)

        client.run_until_disconnected()
