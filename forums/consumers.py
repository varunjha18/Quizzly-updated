import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import message
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async

class ChatRoomConsumer(AsyncWebsocketConsumer):
    def save_to_db(self,message_content,username,user_id):
        # message_content = event['message']
        # username = event['username']
        # user_id = event['user_id']

        save_message=message(forum_name=str(self.room_name),sender_name=str(username),sender_id=int(user_id),content=str(message_content),reply_to=int(0))
        # print(save_message,'sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss')
        save_message.save()
        return 1


    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'forums_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_content = text_data_json['message']
        username = text_data_json['username']
        user_id = text_data_json['user_id']

        

        await self.channel_layer.group_send(
            
            
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message_content,
                'username': username,
                'user_id':user_id,
            }
        )

    async def chatroom_message(self, event):
        message_content = event['message']
        username = event['username']
        user_id = event['user_id']
        flag = await database_sync_to_async(self.save_to_db)(message_content,username,user_id)
        # print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
        # save_to_db(event)
        # save_message=message(forum_name=str(self.room_name),sender_name=str(username),sender_id=int(user_id),content=str(message_content),reply_to=int(0))
        # print(save_message)
        # save_message.save()


        await self.send(text_data=json.dumps({
            'message': message_content,
            'username': username,
            'user_id':user_id,
        }))

    

    pass
