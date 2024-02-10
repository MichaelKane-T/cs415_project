from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cs415.settings import JWT_AUTH
from cs415.authentication import JWTAuthentication
from cs415.models import User,Useraddress,Player,Team
from cs415.serializers import UserSerializer,UseraddressSerializer,PlayerSerializer,TeamSerializer


class Login(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({'success': False,
                             'error': 'Email and Password must have a value'},
                             status = status.HTTP_400_BAD_REQUEST)

        check_user = User.objects.filter(email=email).exists()
        if check_user == False:
            return Response({'success': False,
                             'error': 'User with this email does not exist'},
                             status=status.HTTP_404_NOT_FOUND)

        check_pass = User.objects.filter(email = email, pass_word=password).exists()
        if check_pass == False:
            return Response({'success': False,
                             'error': 'Incorrect password for user'},
                             status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.get(email = email, pass_word=password)

        # add last login to User table
        serializer = UserSerializer(user, data={'last_login': str(datetime.datetime.now())}, partial=True)
        if serializer.is_valid():
            serializer.save()

        if user is not None:
            jwt_token = JWTAuthentication.create_jwt(user)
            data = {
                'token': jwt_token
            }
            return Response({'success': True,
                             'user_id': user.user_id,
                             'token': jwt_token},
                             status=status.HTTP_200_OK)
        else:
            return Response({'success': False,
                             'error': 'Invalid Login Credentials'},
                             status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
 
        if not email or not password:
            return Response({'success': False,
                             'error': 'Email and Password must have a value'},
                             status = status.HTTP_400_BAD_REQUEST)
 
        check_user = User.objects.filter(email=email).exists()
        if check_user == False:
            return Response({'success': False,
                             'error': 'User with this email does not exist'},
                             status=status.HTTP_404_NOT_FOUND)
 
        check_pass = User.objects.filter(email = email, pass_word=password).exists()
        if check_pass == False:
            return Response({'success': False,
                             'error': 'Incorrect password for user'},
                             status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.get(email = email, pass_word=password)
        if user is not None:
            jwt_token = JWTAuthentication.create_jwt(user)
            data = {
                'token': jwt_token
            }
            return Response({'success': True,
                             'token': jwt_token},
                             status=status.HTTP_200_OK)
        else:
            return Response({'success': False,
                             'error': 'Invalid Login Credentials'},
                             status=status.HTTP_400_BAD_REQUEST)

class UserAPIView(APIView):
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})

class UseraddressAPIView(APIView):
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        useraddress = Useraddress.objects.all()
        serializer = UseraddressSerializer(useraddress, many=True)
        return Response({'useraddress': serializer.data})
    
class PlayerAPIView(APIView):
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        player = Player.objects.all()
        serializer = PlayerSerializer(player, many=True)
        return Response({'player': serializer.data})
    
class TeamAPIView(APIView):
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        team = Team.objects.all()
        serializer = TeamSerializer(team, many=True)
        return Response({'team': serializer.data})