from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import message


# Create your views here.
def forums(request):
    return render(request,'base.html')


@login_required(login_url='login')
def room2(request, room_name):
    room_messages=message.objects.filter(forum_name=room_name)
    return render(request, 'chat_room.html', {
        'room_name': room_name,
        'room_messages':room_messages
    })