"""
URL configuration for cs415 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cs415 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.Login.as_view()),
    path('users/', views.UserAPIView.as_view()),
    path('users/<int:user_id>/', views.UserAPIView.as_view()), 
    path('useraddress/', views.UseraddressAPIView.as_view()),
    path('player/', views.PlayerAPIView.as_view()),
    path('team/', views.TeamAPIView.as_view()),
    path('addresses/', views.AddressAPIView.as_view()),
    path('phones/', views.PhoneAPIView.as_view()),
    path('phone-types/', views.PhoneTypeAPIView.as_view()),
    path('address-types/', views.AddressTypeAPIView.as_view()),
    path('user-infos/', views.UserInfoAPIView.as_view()),
    path('pages/', views.PageDataAPIView.as_view()),
    path('addresses/user/<int:user_id>/', views.UseraddressAPIView.as_view(), name='user_addresses'),
    path('phones/user/<int:id>', views.UserPhoneAPIView.as_view()),
    path('pages/page/<int:id>', views.GetSinglePageDataAPIView.as_view()),
    path('users/user/<int:id>',views.GetSingleUserInfoAPIView.as_view()),
    path('users/create_user/', views.CreateUserView.as_view(), name='create_user'),
    path('users/create_player/', views.CreatePlayerView.as_view(), name='create_player'),
    path('users/create_team/', views.CreateTeamView.as_view(), name='create_team'),

]
