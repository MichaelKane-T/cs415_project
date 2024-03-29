import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cs415.models import User, Useraddress, Userphone, Phonetype, Userinfo, Pagedata, Addresstype
from cs415.serializers import UserSerializer, AddressSerializerPost, AddressSerializerGet, PhoneSerializerGet, PhoneSerializerPost
from cs415.serializers import PhoneTypeSerializer, UserinfoSerializer, PageDataSerializer, AddressTypeSerializer
from cs415.settings import JWT_AUTH
from cs415.authentication import JWTAuthentication


class UserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        request.data['created_date'] = str(datetime.datetime.now())
        request.data['is_active'] = 1
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})

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

        check_pass = User.objects.filter(email = email, password=password).exists()
        if check_pass == False:
            return Response({'success': False,
                             'error': 'Incorrect password for user'},
                             status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.get(email = email, password=password)

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


class GetSingleUserAPIView(APIView):
    def get(self,request,id):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        user_data = {}
        user = User.objects.get(pk=id)
        user_serial = UserSerializer(user)
        user_data.update({"user": user_serial.data})
        addresses = AddressSerializerGet(Useraddress.objects.filter(user=user), many=True)
        user_data.update({"addresses": addresses.data})
        info = UserinfoSerializer(Userinfo.objects.filter(user=user), many=True)
        user_data.update({"info": info.data})
        phone = PhoneSerializerGet(Userphone.objects.filter(user=user).select_related(), many=True)
        user_data.update({"phones": phone.data})
        return Response(user_data)

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

class UserAddressAPIView(APIView):
    def get(self,request,id):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        user = User.objects.get(pk=id)
        addresses = Useraddress.objects.filter(user=user)
        serializer = AddressSerializerGet(addresses, many=True)
        return Response({'addresses': serializer.data})

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

class UserPhoneAPIView(APIView):
    def get(self,request,id):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        user = User.objects.get(pk=id)
        phones = Userphone.objects.filter(user=user)
        serializer = PhoneSerializerGet(phones, many=True)
        return Response({'phones': serializer.data})

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
        serializer = UserinfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        user_infos = Userinfo.objects.all()
        serializer = UserinfoSerializer(user_infos, many=True)
        return Response({'user_infos': serializer.data})

class GetSingleUserInfoAPIView(APIView):
    def get(self,request,id):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        user = User.objects.get(pk=id)
        info = Userinfo.objects.filter(user=user)
        serializer = UserinfoSerializer(info, many=True)
        return Response({'info': serializer.data})

class GetSinglePageDataAPIView(APIView):
    def get(self,request,id):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        page = Pagedata.objects.get(pk=id)
        serializer = PageDataSerializer(page)
        return Response({'page': serializer.data})