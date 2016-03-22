from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings
from rest_framework import viewsets
from game.models import Character, Room
from .serializers import CharacterSerializer, RoomSerializer

class LoginView(TemplateView):
  template_name = 'login.html'

  def post(self, request, **kwargs):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )
    return render(request, self.template_name)

class LogoutView(TemplateView):
  template_name = 'logout.html'
  def get(self, request, **kwargs):
    logout(request)
    return render(request, self.template_name)

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer