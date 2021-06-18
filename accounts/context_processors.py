from .models import User_profile
from django.shortcuts import get_object_or_404, render

def user_profile(request):
    if request.user.is_authenticated:
        user_profile=get_object_or_404(User_profile,user_id=request.user.id)
        return {'user_profile' : user_profile ,}
    else:
        return {}