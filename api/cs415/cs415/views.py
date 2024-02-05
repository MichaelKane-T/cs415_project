from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cs415.models import User
from cs415.serializers import UserSerializer


class UserAPIView(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})