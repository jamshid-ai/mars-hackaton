from django.db import models

class Quiz(models.Model):
    label = models.CharField(max_length=200)
    quiz_photo = models.ImageField(null=True)

    def __str__(self):
        return self.label
   

class Question(models.Model):
    RIGHT_OPT = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3')
    )  
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='question')
    question = models.CharField(max_length=200)
    rightAnswerId = models.IntegerField(choices=RIGHT_OPT, default=0)

    def __str__(self):
        return self.question
    
    
    
class Answers(models.Model):
    text = models.CharField(max_length=200)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    
    
    def __str__(self):
        return self.text
    