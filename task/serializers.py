from rest_framework import serializers
from .models import Question, Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id','user', 'title', 'image','image_url', 'created_at', 'question']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True, source='answer_set')

    class Meta:
        model = Question
        fields = ['id','user', 'title', 'image','image_url', 'status', 'answers']
        extra_kwargs = {
            'image': {'required': True},  # Ensure `image` is required
        }
