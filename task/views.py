from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer,QuestionDetailSerializer

class QuestionListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        questions = Question.objects.filter(user=request.user)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id  # Foydalanuvchini autentifikatsiyadan kelgan ma'lumotga sozlash
        serializer = QuestionSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AnswerListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, question_id):
        # Get answers related to a specific question
        answers = Answer.objects.filter(question__id=question_id)
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)

    def post(self, request, question_id):
        # Add the authenticated user and associate the answer with a question
        data = request.data.copy()
        data['user'] = request.user.id
        data['question'] = question_id
        serializer = AnswerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class QuestionDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            question = Question.objects.prefetch_related('answers').get(pk=pk, user=request.user)
            serializer = QuestionDetailSerializer(question)
            return Response(serializer.data)
        except Question.DoesNotExist:
            return Response({'error': 'Question not found'}, status=404)
