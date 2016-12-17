from django.db import models

# Create your models here.


class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return "User("+self.login+")"
    

