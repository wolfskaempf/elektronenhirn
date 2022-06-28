import base64
import logging

from aiohttp.web import BaseRequest
from opsdroid.events import Message
from opsdroid.matchers import match_crontab, match_webhook
from opsdroid.skill import Skill

_LOGGER = logging.getLogger(__name__)


class Tops(Skill):
    def __init__(self, opsdroid, config):
        super(Tops, self).__init__(opsdroid, config)
        # Load custom configuration part
        # self.conf = self.opsdroid.config['skills']['tops']['config']

    @match_webhook('top_create')
    async def top_create(self, event: BaseRequest):
        data = await event.json()
        await self.opsdroid.send(Message(str(data['message'])))

    # matches every Tuesday at 15:00
    @match_crontab('00 15 * * 2', timezone="Europe/Berlin")
    async def info_send(self, event):
        reminder_message_base64 = self.opsdroid.config['skills']['tops']['reminder-message']
        reminder_message = base64.b64decode(reminder_message_base64.encode()).decode()

        await self.opsdroid.send(Message(text=reminder_message))
