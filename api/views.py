from rest_framework.generics import ListAPIView
from .serializers import QuizSerializer, QuestionSerializer, Answers
from .models import Quiz, Question, Answers 

class QuizAPIView(ListAPIView):
    
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    
class QuestionAPIView(ListAPIView):
    
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer