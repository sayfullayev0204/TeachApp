# from django.contrib.auth.models import User
# from django.contrib.auth import  login, logout
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from rest_framework_simplejwt.tokens import RefreshToken

# # Ro'yxatdan o'tish
# @api_view(['POST'])
# def register(request):
#     username = request.data.get('username')
#     password = request.data.get('password')

#     if User.objects.filter(username=username).exists():
#         return Response({'error': 'Bu foydalanuvchi allaqachon mavjud!'}, status=status.HTTP_400_BAD_REQUEST)

#     user = User.objects.create_user(username=username, password=password)
#     return Response({'message': 'Foydalanuvchi muvaffaqiyatli ro\'yxatdan o\'tdi!'})

# @api_view(['POST'])
# def login_view(request):
#     username = request.data.get('username')
#     password = request.data.get('password')

#     if not username:
#         return Response({'error': 'Username kiritilmagan!'}, status=status.HTTP_400_BAD_REQUEST)

#     if not User.objects.filter(username=username).exists():
#         return Response({'error': 'Bunday foydalanuvchi mavjud emas!'}, status=status.HTTP_404_NOT_FOUND)

#     if not password:
#         return Response({'error': 'Parol kiritilmagan!'}, status=status.HTTP_400_BAD_REQUEST)

#     user = User.objects.get(username=username)
#     if not user.check_password(password):
#         return Response({'error': 'Parol noto\'g\'ri!'}, status=status.HTTP_400_BAD_REQUEST)

#     login(request, user)
#     refresh = RefreshToken.for_user(user)
#     return Response({
#         'message': 'Tizimga muvaffaqiyatli kirildi!',
#         'refresh': str(refresh),
#         'access': str(refresh.access_token)
#     })
# # Tizimdan chiqish
# @api_view(['POST'])
# def logout_view(request):
#     logout(request)
#     return Response({'message': 'Tizimdan chiqildi!'}, status=status.HTTP_200_OK)
