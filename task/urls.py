from django.urls import path
from .views import QuestionListCreateAPIView, AnswerCreateAPIView, ActiveQuestionListAPIView


urlpatterns = [
    path('questions/', QuestionListCreateAPIView.as_view(), name='question-list-create'),
    path('answers/', AnswerCreateAPIView.as_view(), name='answer-create'),
    path('questions/active/', ActiveQuestionListAPIView.as_view(), name='active-questions'),
]
