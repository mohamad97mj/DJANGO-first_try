from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):

    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, None)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "{}-choice".format(self.question)


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)

    def __str__(self):
        return "{}-token".format(self.user)


class NewUser(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_address = models.EmailField()
