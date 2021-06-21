from django.shortcuts import render
from .models import Score

# Create your views here.

def leaderboard(request,quiz_id):
    this_quiz_leaderboard=Score.objects.filter(quiz_id=quiz_id).order_by('-score')
    rank=1
    quantity=0
    current_score=this_quiz_leaderboard[0].score
    ranks=[]
    for people in this_quiz_leaderboard:
        if people.score<current_score:
            rank+=quantity
            quantity=0
        else:
            quantity+=1
        ranks.append(rank)
         
    # print(this_quiz_leaderboard.count())
    score_count=this_quiz_leaderboard.count()
    data={'scores':zip(this_quiz_leaderboard,ranks)}
    return render(request,'leaderboard.html',data)