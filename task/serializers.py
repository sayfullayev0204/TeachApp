from rest_framework import serializers
from .models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'image', 'created_at', 'status', 'image_url', 'user']

    def create(self, validated_data):
        # Foydalanuvchini kontekstdan olib, savolga biriktiramiz
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)

class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Display username instead of ID

    class Meta:
        model = Answer
        fields = ['id', 'question', 'title', 'image', 'created_at', 'image_url', 'user']
