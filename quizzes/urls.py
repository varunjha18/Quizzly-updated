from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('<int:quiz_id>/start_quiz',views.start_quiz,name='start_quiz'),
   path('<int:quiz_id>',views.question,name='question'),
   path('view_questions/<int:quiz_id>',views.view_questions,name='view_questions'),
   path('create_quiz',views.create_quiz,name='create_quiz'),
   path('create_questions/<int:quiz_id>/<int:no_of_ques>',views.create_questions,name='create_questions'),
   path('edit_question/<int:quiz_id>/<int:question_no>',views.edit_question,name='edit_question'),
   # path('<int:quiz_id>',views.question,name='question'),
]