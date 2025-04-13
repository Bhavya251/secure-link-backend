import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.room_name = f"user_{self.user.id}"
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        await self.send(text_data=json.dumps({"message": "WebSocket connected ✅"}))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        receiver_id = data['receiver_id']
        session_id = data['session_id']
        attachment = data.get('attachment')  # optional

        # Save message to DB
        from accounts.models import User, Message
        receiver = await database_sync_to_async(User.objects.get)(id=receiver_id)
        await database_sync_to_async(Message.objects.create)(
            sender=self.user,
            receiver=receiver,
            content=message,
            session_id=session_id
        )

        # Send message to the receiver’s group
        await self.channel_layer.group_send(
            f"chat_user_{receiver_id}",
            {
                'type': 'chat_message',
                'message': message,
                'sender_id': self.user.id,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender_id': event['sender_id'],
        }))
