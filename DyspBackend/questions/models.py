from django.db import models
from datetime import datetime



class UserInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=13)
    location = models.CharField(max_length=100)
    password = models.CharField(max_length=15)
    interests = models.CommaSeparatedIntegerField
    bio = models.CharField(max_length=30)
    photo = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name +"- "+ self.bio

class Question(models.Model):
    question = models.CharField(max_length=100)
    creator = models.CharField(max_length=50)
    views = models.BigIntegerField
    report = models.IntegerField
    no_answers = models.IntegerField
    tags = models.CommaSeparatedIntegerField
    #date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.question +"- "+ self.creator


class Answer(models.Model):
    answer = models.CharField(max_length=500)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    upvotes = models.IntegerField
    views = models.BigIntegerField
    report = models.IntegerField
    #date = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.answer +"- "+ str(self.upvotes)


class Upvotes(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user_upvotes = models.ForeignKey(UserInfo, on_delete=models.CASCADE)