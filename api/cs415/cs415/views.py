from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from rest_framework import status
from cs415.settings import JWT_AUTH
from cs415.authentication import JWTAuthentication
from cs415.models import User,Useraddress,Player,Team,UserInfo,Pagedata,Userphone,Addresstype,Phonetype
from cs415.serializers import UserSerializer,UseraddressSerializer,PlayerSerializer,TeamSerializer,PageDataSerializer,UserInfoSerializer,AddressSerializerPost,AddressSerializerGet, PhoneSerializerPost, PhoneSerializerGet,PhoneTypeSerializer, AddressTypeSerializer


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
        serializer = UserSerializer(user, data={'last_login': str(datetime.now())}, partial=True)
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
    

class UserAPIView(APIView):
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})

class UseraddressAPIView(APIView):
    def get(self, request, user_id):
        # Check authentication if JWT_AUTH is True
        if JWT_AUTH:
            JWTAuthentication().authenticate(request=request)

        useraddresses = Useraddress.objects.filter(user=user_id)
        serializer = UseraddressSerializer(useraddresses, many=True)
        return Response({'useraddress': serializer.data})
    

class AddressAPIView(APIView):
    def post(self, request, *args, **kwargs):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        serializer = AddressSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        user_addresses = Useraddress.objects.all()
        serializer = AddressSerializerGet(user_addresses, many=True)
        return Response({'user_addresses': serializer.data})
    
class PhoneAPIView(APIView):
    def post(self, request, *args, **kwargs):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        serializer = PhoneSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        user_phones = Userphone.objects.all()
        serializer = PhoneSerializerGet(user_phones, many=True)
        return Response({'user_phones': serializer.data})

class PhoneTypeAPIView(APIView):
    def post(self, request, *args, **kwargs):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        serializer = PhoneTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        phone_types = Phonetype.objects.all()
        serializer = PhoneTypeSerializer(phone_types, many=True)
        return Response({'phone_types': serializer.data})
        
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
    
class GetSingleUserInfoAPIView(APIView):
    def get(self,request,id):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        user = User.objects.get(pk=id)
        info = UserInfo.objects.filter(user=user)
        serializer = UserInfoSerializer(info, many=True)
        return Response({'info': serializer.data})

class GetSinglePageDataAPIView(APIView):
    def get(self,request,id):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        page = Pagedata.objects.get(pk=id)
        serializer = PageDataSerializer(page)
        return Response({'page': serializer.data})
class AddressTypeAPIView(APIView):
    def post(self, request, *args, **kwargs):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        serializer = AddressTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        address_types = Addresstype.objects.all()
        serializer = AddressTypeSerializer(address_types, many=True)
        return Response({'address_types': serializer.data})

class UserInfoAPIView(APIView):
    def post(self, request, *args, **kwargs):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        user_infos = UserInfo.objects.all()
        serializer = UserInfoSerializer(user_infos, many=True)
        return Response({'user_infos': serializer.data})

class PageDataAPIView(APIView):
    def post(self, request, *args, **kwargs):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        serializer = PageDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        page_datas = Pagedata.objects.all()
        serializer = PageDataSerializer(page_datas, many=True)
        return Response({'pages': serializer.data})

class UserPhoneAPIView(APIView):
    def get(self,request,id):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        user = User.objects.get(pk=id)
        phones = Userphone.objects.filter(user=user)
        serializer = PhoneSerializerGet(phones, many=True)
        return Response({'phones': serializer.data})
    
class CreateUserView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data

        # Create a user
        user_data = {
            'first_name': data.get('first_name'),
            'second_name': data.get('second_name'),
            'pass_word': data.get('pass_word'),
            'recovery_key': data.get('recovery_key'),
            'date_created': datetime.now(),
            'email': data.get('email'),  # Use the email from the request
        }

        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            # Save the user data
            user_serializer.save()

            # Extract user_id from the newly created user
            user_id = user_serializer.data.get('user_id')

            # Create a Useraddress associated with the user
            user_address_data = {
                'address_1': data.get('address_1'),
                'address_2': data.get('address_2'),
                'city': data.get('city'),
                'zip': data.get('zip'),
                'country': data.get('country'),
                'email': data.get('email'),  # Use the email from the request
                'user': user_id,
                'last_date_updated': datetime.now(),
            }

            # Serialize and save the Useraddress data
            user_address_serializer = UseraddressSerializer(data=user_address_data)
            if user_address_serializer.is_valid():
                user_address_serializer.save()

                # Create a combined response
                response_data = {
                    'user': user_serializer.data,
                    'user_address': user_address_serializer.data,
                }

                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                # Delete the user if the associated Useraddress creation fails
                User.objects.filter(user_id=user_id).delete()
                return Response({'error': 'Failed to create Useraddress', 'details': user_address_serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Failed to create User', 'details': user_serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

class CreatePlayerView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class CreateTeamView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)