from rest_framework.views import APIView
from account.serializers import RegisterSerializer, ForgotPasswordSerializer,ForgotPasswordCompleteSerializer, ProfileSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

User = get_user_model()

class RegisterAPIView(APIView): # Пост запрос на регистрацию
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Вы успешно зарегистрировались. Вам отправлено письмо с активацией на вашу почту.', status=201)

class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response('Активация аккаунта прошла успешно.', status=200)
        except User.DoesNotExist:
            return Response('Ссылка уже была использована.', status=400)
        
class EditProfileAPIView(generics.RetrieveUpdateAPIView): # Put & Patch на изменение данных профиля
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.queryset.get(id=self.request.user.id)

class GetProfile(generics.ListAPIView): # Просмотр профиля (себя)
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)