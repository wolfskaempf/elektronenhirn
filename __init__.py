from opsdroid.matchers import match_regex, match_webhook
from opsdroid.skill import Skill
from opsdroid.events import Message

from aiohttp.web import BaseRequest

import logging
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
