from rest_framework import serializers
from .models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['category', 'title', 'image', 'status']
        extra_kwargs = {
            'image': {'required': True}  # Make sure `image` is required if it must be sent with the POST request
        }
            
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
