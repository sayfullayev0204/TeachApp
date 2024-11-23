from django.urls import path
from .views import QuestionListCreateAPIView, AnswerListCreateAPIView

urlpatterns = [
    path('questions/', QuestionListCreateAPIView.as_view(), name='question_list_create'),
    path('questions/<int:question_id>/answers/', AnswerListCreateAPIView.as_view(), name='answer_list_create'),
]
