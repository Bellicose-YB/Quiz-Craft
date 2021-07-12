# from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Quiz(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    QuizTitle = models.CharField(max_length=100)
    time = models.DurationField(help_text="Duration of the Quizin format HH:MM:SS")
    score = models.IntegerField(help_text="Total score of the Quiz", blank = True)
    # created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.QuizTitle}"
    
    def getQuestions(self):
        return self.Questions_set.all()

class Questions(models.Model):
    AuthorKey = models.ForeignKey(User, on_delete=models.CASCADE)
    QuizKey = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    Score = models.IntegerField(help_text="Score of this question", default=4)
    Statement = models.TextField()
    CorrectOption = models.TextField()     
    OtherOption1 = models.TextField()     
    OtherOption2 = models.TextField()     
    OtherOption3 = models.TextField()     
    
    def __str__(self):
        return f"{self.QuizKey.QuizTitle}"

