import json
from channels.generic.websocket import AsyncWebsocketConsumer


class MonitorConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.group_name = 'monitor'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.grou_name, self.channel_name)

    async def broadcast_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))