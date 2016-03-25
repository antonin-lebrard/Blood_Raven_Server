# Create your views here.

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from game.serializers import CharacterSerializer, RoomSerializer
from rest_framework import viewsets
from game.models import Character, Room, Portal
from game.forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect(play)# Redirect to a success page.
    return render(request, 'login.html', {'login_form': form })

@login_required
def play(request):
    user = request.user
    username = user.get_username()
    char = None
    room_id = None
    try:
        char = Character.objects.filter(Q(user=user))[0]
        char_name = char.name
        room_id = char.room.name
        portal_available = Portal.objects.filter(Q(entry=char.room))
    except Character.DoesNotExist:
        pass # redirect to createchar.html
    except Exception:
        pass # ne rien faire bien sur
    return render(request, 'play.html', locals())
    # redirect to /game/play (Anto)
    # qui effectue une requete /api/char_status
    # j'identifie de cette façon request.user.char et renvoie
    # {
    #   "name": "Conan",
    # toutes les infos > plusierus requetes
	#   "room": "/api/room/room_id"
    # }

def logout_view(request):
    if request.user.is_authenticated():
        logout(request)
    return  HttpResponseRedirect('/home')

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
