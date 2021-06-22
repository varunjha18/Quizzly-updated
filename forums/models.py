from django.db import models

# Create your models here.
class forum(models.Model):
    forum_name=models.CharField(max_length=100)  
    # this would be quiz id , its a number but will be treated as a string 
    forum_code=models.CharField(max_length=100,blank=True)
    forum_image=models.ImageField(upload_to="photos/%y/%m/",blank=True,default='aaaaaaa.jpeg')



class message(models.Model):
    forum_name=models.CharField(max_length=100)  
    sender_name=models.CharField(max_length=150)  
    sender_id=models.IntegerField(default=0)     # user_id of the sender
    content=models.TextField(max_length=5000)     #message
    reply_to=models.IntegerField(blank=True,default=None)    # id of the message if it is a reply to it 

    def __str__(self):
        return str(self.sender_name)