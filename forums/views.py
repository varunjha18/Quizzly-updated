from django.shortcuts import render
from django.contrib.auth.decorators import login_required



# Create your views here.
def forums(request):
    return render(request,'base.html')


@login_required(login_url='login')
def room2(request, room_name):

    return render(request, 'chat_room.html', {
        'room_name': room_name,
    })