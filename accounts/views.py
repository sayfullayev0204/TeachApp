from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .models import User
from .serializers import UserSerializer


class RegisterAPIView(APIView):
    """
    API endpoint for user registration without requiring tokens.
    """

    def post(self, request, *args, **kwargs):
        data = request.data

        # Required fields for user registration
        required_fields = ["username", "password", "first_name", "last_name"]
        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            return Response(
                {"error": f"Missing fields: {', '.join(missing_fields)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )



        # Check if username is already taken
        if User.objects.filter(username=data["username"]).exists():
            return Response(
                {"error": "Username is already taken."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            # Create a new user
            user = User.objects.create(
                username=data["username"],
                password=make_password(data["password"]),
                first_name=data["first_name"],
                last_name=data["last_name"],
            )

            # Serialize and return the user data
            serializer = UserSerializer(user)

            return Response(
                {"message": "User registered successfully", "user": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response(
                {"error": f"Failed to register user: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
