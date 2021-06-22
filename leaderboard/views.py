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
    if request.user.is_authenticated:
        this_user_score=Score.objects.filter(quiz_id=quiz_id,user_id=request.user.id)
        if this_user_score.exists():
            user_ranking=Score.objects.values_list('score', flat=True)
            user_rank=len(user_ranking)+1
            for i in range(len(user_ranking)):
                if this_user_score[0].score>=user_ranking[i]:
                    user_rank=i+1
                    break
            
            data={'scores':zip(this_quiz_leaderboard,ranks),
                    'this_user_score':this_user_score[0],
                    'this_user_rank':user_rank,
            }
            
        else:    
            data={'scores':zip(this_quiz_leaderboard,ranks)}
    else:
        data={'scores':zip(this_quiz_leaderboard,ranks)}

    return render(request,'leaderboard.html',data)