from os import truncate
from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField

option_choices=(('A','A'),
('B','B'),
('C','C'),
('D','D'),
)
# Create your models here.
class Question(models.Model):
    quiz_id=models.IntegerField(default=id)
    question_no=models.IntegerField()
    problem=models.TextField()
    option_1=models.CharField(max_length=200)
    option_2=models.CharField(max_length=200)
    option_3=models.CharField(max_length=200,default='Both of these')
    option_4=models.CharField(max_length=200,default='None of these')
    correct_answer=models.CharField(max_length=10)
    prob_img_1=models.ImageField(upload_to="photos/%y/%m/",blank=True)
    prob_img_2=models.ImageField(upload_to="photos/%y/%m/",blank=True)
    points=models.IntegerField(default=10)
    date_created=models.DateTimeField(blank=True,default=datetime.now())

    def __str__(self):
        return str(self.quiz_id)



class Quiz(models.Model):
    quiz_id=models.IntegerField()
    private_key=models.CharField(max_length=50,blank=True)
    quiz_title=models.CharField(max_length=200)
    quiz_sub_heading=models.CharField(max_length=200,blank=True)
    cover_img=models.ImageField(upload_to="photos/%y/%m/",default='aaaaaaa.jpeg')
    created_by=models.IntegerField(default=1)
    is_public=models.BooleanField(default=True)
    instructions=models.TextField(blank=True)
    time_alloted=models.IntegerField(default=20)

  



    def __str__(self):
        return str(self.quiz_id)