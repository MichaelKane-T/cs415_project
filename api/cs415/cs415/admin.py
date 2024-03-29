from django.contrib import admin
from .models import User, Useraddress, Userinfo, Userphone, Pagedata, Phonetype, Addresstype

admin.site.register(User)
admin.site.register(Useraddress)
admin.site.register(Userinfo)
admin.site.register(Userphone)
admin.site.register(Pagedata)
admin.site.register(Phonetype)
admin.site.register(Addresstype)