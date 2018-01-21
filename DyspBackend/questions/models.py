from django.db import models


class UserInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    dob = models.parse_date
    contact_no = models.CharField(max_length=13)
    location = models.CharField()
    password = models.CharField(min_lengt=6)
    interests = models.CommaSeparatedIntegerField
    bio = models.CharField(max_length=30)
    photo = models.CharField(maxlength=100)


class Question(models.Model):
    question = models.CharField(max_length=100)
    creator = models.CharField(max_length=50)
    views = models.BigIntegerField
    report = models.IntegerField
    no_answers = models.IntegerField
    tags = models.CommaSeparatedIntegerField


class Answer(models.Model):
    answer = models.CharField(max_length=500)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    upvotes = models.IntegerField
    views = models.BigIntegerField
    report = models.IntegerField


class Upvotes(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user_upvotes = models.ForeignKey(UserInfo, on_delete=models.CASCADE)