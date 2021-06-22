from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import message
from quizzes.models import Quiz
from .models import forum


# Create your views here.
def forums(request):
    return render(request,'base.html')


@login_required(login_url='login')
def room2(request, room_name):
    # this_room=forum.objects.filter(forum_name=room_name)
    this_room=Quiz.objects.filter(quiz_id=room_name)
    room_messages=message.objects.filter(forum_name=room_name)
    return render(request, 'chat_room.html', {
        'room_name': room_name,
        'room_messages':room_messages,
        'this_forum':this_room[0]
    })