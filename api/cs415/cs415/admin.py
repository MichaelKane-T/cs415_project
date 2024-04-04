from django.contrib import admin
from .models import Player, Team,User,Useraddress,UserInfo

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(User)
admin.site.register(Useraddress)
admin.site.register(UserInfo)