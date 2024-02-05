from rest_framework import serializers
from cs415.models import User,Useraddress,Team,Player

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all_'

class UseraddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Useraddress
        fields = '__all_'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'