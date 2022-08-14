from django.urls import path

from .views import QuizAPIView, QuestionAPIView

urlpatterns = [
    path('quiz/', QuizAPIView.as_view(), name='quiz_list'),
    path('qestion/', QuestionAPIView.as_view(), name='question_list'),
]
