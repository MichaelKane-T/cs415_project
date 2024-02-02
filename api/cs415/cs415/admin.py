from django.contrib import admin
from .models import Player, Team,User,Useraddress

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(User)
admin.site.register(Useraddress)
