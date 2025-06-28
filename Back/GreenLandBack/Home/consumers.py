import json
from channels.generic.websocket import AsyncWebsocketConsumer

class GreenLandConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.greenland_id = self.scope['url_route']['kwargs']['greenland_id']
        self.group_name = f'greenland_{self.greenland_id}'

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):

        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'send_update',
                'message': data.get('message', '')
            }
        )

    async def send_update(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))
