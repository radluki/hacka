from django.db import models

# Create your models here.


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()
    date = models.DateTimeField('location time')

    def __str__(self):
        return "User("+self.login+")"


class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    question_text = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')
    answer = models.CharField(max_length=200)
    user_id = models.ForeignKey(User)
    def __str__(self):
        return self.question_text
    
