from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from quizzes.models import Quiz
from quizzes.models import Question
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from leaderboard.models import Score
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    all_quizzes=Quiz.objects.all()
    if request.method=='POST':
        query=request.POST.get('search')
        all_quizzes=all_quizzes.filter(quiz_title__icontains=query)


    data={'all_quizzes':all_quizzes}
    return render(request,'home.html',data)


def start_quiz(request,quiz_id):
    quiz_start= get_object_or_404(Quiz,pk=quiz_id)
    # print('sbsfndfnnnnnnnnnnnnnnnnnnnnnnnnnnd dddddddddddddddddddddddddddddddddddd')
    data={
        'quiz_start':quiz_start,
    }
    return render(request,"quiz_start.html",data)



def question(request,quiz_id):
    questions = Question.objects.filter(quiz_id=quiz_id)
    # alpha_options=['A','B','C','D']
    # model_options=['option_1','option_2','option_3','option_4']
    result=[]
    if request.method=="POST":
        score=0
        for i in range(len(questions)):
            # print(request.POST.get('question-'+str(i+1)+'-answers'))
            ans_given=(request.POST.get('question-'+str(i+1)+'-answers'))
            
            if ans_given=="A":
                ans_given_full=questions[i].option_1
            elif ans_given=='B':
                ans_given_full=questions[i].option_2
            elif ans_given=='C':
                ans_given_full=questions[i].option_3
            elif ans_given=='D':
                ans_given_full=questions[i].option_4
            else:
                ans_given_full='Not Answered'

            right_ans=questions[i].correct_answer
            
            if ans_given=='B':
                right_ans_full=questions[i].option_2
            elif ans_given=='C':
                right_ans_full=questions[i].option_3
            elif ans_given=='D':
                right_ans_full=questions[i].option_4
            else:
                right_ans_full=questions[i].option_1
            


            if ans_given==None:
                result.append([-1,questions[i].problem,ans_given_full,right_ans_full])
            elif str(ans_given)==str(right_ans):
                result.append([1,questions[i].problem,ans_given_full,right_ans_full])
                score+=questions[i].points
            else:
                result.append([0,questions[i].problem,ans_given_full,right_ans_full])
        
        # print(result)
        user_id=request.user.id
        # print(user_id)
        # print('jvhjhhhvjfuyfvjadvaaav')

        if user_id is not None:
            user_name=str(request.user.first_name)+' '+str(request.user.last_name)
            previous_high=Score.objects.filter(quiz_id=quiz_id,user_id=user_id)
            
            

            # print(previous_high,'ggggggggggggggggggggggggg')
            if previous_high.exists():
                previous_high=previous_high[0]
                if score>previous_high.score:
                    previous_high.score=score
                    previous_high.save()
            else:
                new_high=Score(quiz_id=quiz_id,user_id=user_id,score=score,user_name=user_name)
                new_high.save()

        ranking=Score.objects.values_list('score', flat=True)
        rank=len(ranking)+1
        for i in range(len(ranking)):
            if score>=ranking[i]:
                rank=i+1
                break

        res_data={
            'result':result,
            "score":score,
            'rank':rank,
        }


        return render(request,"results.html",res_data)
        


    data={
        'questions':questions,
        'quiz_id':quiz_id,
    }
    return render(request,"questions.html",data)


@login_required(login_url='login')
def create_quiz(request):
    new_quiz_id=max(Quiz.objects.values_list('id',flat=True))+1
    print(new_quiz_id,'nnnnneeeewwwww_____qqqquuuuiiiiizzzzzz_____iiiiiidddd')
    if request.method=="POST":
              
        quiz_title=request.POST.get('quiz_title')
        quiz_sub_heading=request.POST.get('quiz_sub_heading')
        cover_img=request.FILES.get('cover_img')
        no_of_ques=int(request.POST.get('no_of_ques'))
        instructions=(request.POST.get('instructions'))
        # print(no_of_ques,quiz_title,'wevwrvwefwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')
        # print(Quiz.objects.values_list('id',flat=True))
        if cover_img==None:
            cover_img='../media/aaaaaaa.jpeg'
        quiz=Quiz(quiz_id=new_quiz_id,quiz_title=quiz_title,cover_img=cover_img,created_by=request.user.id,instructions=instructions,quiz_sub_heading=quiz_sub_heading)

        quiz.save()
        # data={'no_of_ques' : range(int(no_of_ques)) }
        return redirect('create_questions',new_quiz_id,no_of_ques)

    return render(request,'create_quiz_start.html',{'new_quiz_id':new_quiz_id})



def create_questions(request,quiz_id,no_of_ques):
    data={'no_of_ques' : range(1,int(no_of_ques)+1) ,'quiz_id':quiz_id,'number':int(no_of_ques)}
    if request.method=='POST':
        
        for j in range(no_of_ques):
            problem=request.POST.get('problem-'+str(j+1))
            print(problem)
            if problem is not None and problem is not "":
                question_no=j+1
                option_1=request.POST.get('question-'+str(j+1)+'-option-1')
                option_2=request.POST.get('question-'+str(j+1)+'-option-2')
                option_3=request.POST.get('question-'+str(j+1)+'-option-3')
                option_4=request.POST.get('question-'+str(j+1)+'-option-4')
                correct_ans=request.POST.get('question-'+str(j+1)+'-correct')
                prob_img_1=request.FILES.get( 'image-'+str(j+1))
                # print('gjwvfjkbkjbijkjkbwfewev')
            # print(problem,question_no,option_1,option_2,option_3,option_4,option_5,correct_ans)

                question=Question(quiz_id=quiz_id,problem=problem,question_no=question_no,option_1=option_1,option_2=option_2,option_3=option_3,option_4=option_4,correct_answer=correct_ans,prob_img_1=prob_img_1)

                question.save()
    
        return redirect('home')

    if request.method=="GET":
        if request.GET.get('action') =='new_no_ques':
            # print('gvjhvqjhkjbjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
            return redirect('create_questions',quiz_id,request.GET.get('new_no_ques'))

    return render(request,'create_questions.html',data)









def view_questions(request,quiz_id):
    all_questions=Question.objects.filter(quiz_id=quiz_id)
       
    
    data={
        'all_questions':all_questions,
        'quiz_id':quiz_id,
    }
    return render(request,'view_questions.html',data)


def edit_question(request,quiz_id,question_no):
    if request.method=='POST':
        print(request.POST.get('problem','nope'),'wewnevkjwbevw,vejw,evw,vwj,')
    
    question=get_object_or_404(Question,quiz_id=quiz_id,question_no=question_no)
    data={'question':question}

    return render(request,'edit_question.html',data)