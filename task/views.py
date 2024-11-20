from rest_framework import generics, permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
from django.http import HttpResponse
class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def post(self, request, *args, **kwargs):
        # Handle file uploads
        data = request.data
        data['image'] = request.FILES.get('image', None)  # Get uploaded file if present
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class ActiveQuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.filter(status=True)
    serializer_class = QuestionSerializer

class QuestionDetailAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def retrieve(self, request, *args, **kwargs):
        # Get the question instance
        question = self.get_object()
        question_serializer = self.get_serializer(question)

        # Get related answers
        answers = Answer.objects.filter(question=question)
        answer_serializer = AnswerSerializer(answers, many=True)

        # Combine question and answers in a single response
        response_data = {
            'question': question_serializer.data,
            'answers': answer_serializer.data,
        }
        return Response(response_data)

def py(request):
    return HttpResponse("Hello, world. 86c34004 is the polls index.")