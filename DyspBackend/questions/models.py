from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=13)

    #def __str__(self):
     #   return self.first_name +"- "+ self.last_name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

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

