from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date is published")
    votes = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.question_text

class Answer(models.Model):
    question_ref = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.text
