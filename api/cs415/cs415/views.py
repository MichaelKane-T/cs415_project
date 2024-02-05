from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cs415.models import User,Useraddress,Player,Team
from cs415.serializers import UserSerializer,UseraddressSerializer,PlayerSerializer,TeamSerializer


class UserAPIView(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})

class UseraddressAPIView(APIView):
    def get(self,request):
        useraddress = Useraddress.objects.all()
        serializer = UseraddressSerializer(useraddress, many=True)
        return Response({'useraddress': serializer.data})
    
class PlayerAPIView(APIView):
    def get(self,request):
        player = Player.objects.all()
        serializer = PlayerSerializer(player, many=True)
        return Response({'player': serializer.data})
    
class TeamAPIView(APIView):
    def get(self,request):
        team = Team.objects.all()
        serializer = TeamSerializer(team, many=True)
        return Response({'team': serializer.data})