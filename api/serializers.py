from rest_framework import serializers

from .models import Quiz, Question, Answers

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id','name')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ('text', 'questin_id')
        
class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ('quiz_id', 'question', 'answer')
        
        
        
