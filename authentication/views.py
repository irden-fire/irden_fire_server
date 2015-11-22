from django.contrib.auth.models import User
from authentication.models import UserData
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from authentication.serializers import UserSerializer
from authentication.serializers import UserDataSerializer

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CurrentUserView(APIView):
    def get(self, request):
        e = UserData.objects.get(user=request.user)
        serializer = UserDataSerializer(e)
        return Response(serializer.data)
