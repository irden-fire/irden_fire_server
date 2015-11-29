from django.contrib.auth.models import User
from authentication.models import UserData
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from authentication.serializers import UserSerializer
from authentication.serializers import UserSerializerCreate
from authentication.serializers import UserDataSerializer

class UserListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    model = User
    serializer_class = UserSerializerCreate

class CreateUserDataView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    model = UserData
    serializer_class = UserDataSerializer

class CurrentUserView(APIView):
    def get(self, request):
        e = UserData.objects.get(user=request.user)
        serializer = UserDataSerializer(e)
        return Response(serializer.data)
