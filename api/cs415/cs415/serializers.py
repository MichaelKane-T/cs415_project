from rest_framework import serializers
from cs415.models import User,Useraddress,Team,Player,UserInfo,Pagedata,Userphone,Addresstype,Phonetype

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UseraddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Useraddress
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserInfo
        fields='__all__'

class PageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model= Pagedata
        fields='__all__'

class AddressTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Addresstype
        depth=1
        fields = '__all__'

class AddressSerializerGet(serializers.ModelSerializer):
    address_type = AddressTypeSerializer(read_only=True)
    class Meta:
        model = Useraddress
        # depth = 1
        fields = '__all__'


class AddressSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Useraddress
        fields = '__all__'

class PhoneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Phonetype
        depth=1
        fields = '__all__'

class PhoneSerializerGet(serializers.ModelSerializer):
    phone_type = PhoneTypeSerializer(read_only=True)
    class Meta:
        model=Userphone
        fields = '__all__'


class PhoneSerializerPost(serializers.ModelSerializer):
    class Meta:
        model=Userphone
        fields = '__all__'

