# Create your views here.

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from game.serializers import CharacterSerializer, RoomSerializer, UserSerializer
from rest_framework import viewsets
from game.models import Character, Room, Portal
from game.forms import LoginForm
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from game.forms import NewCharacterFrom
from rest_framework.views import APIView


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect(play2)# Redirect to a success page.
    return render(request, 'login.html', {'login_form': form })

@login_required
def play2(request):
    user = request.user
    username = user.get_username()
    char = None
    room_id = None
    try:
        char = Character.objects.get(Q(user=user))
        char_name = char.name
        room_id = char.room.name
        char_avatar = char.avatar.url
        portal_available = Portal.objects.filter(Q(entry=char.room))
    except Character.DoesNotExist:
        return redirect(CreateCharacter)
    except Exception:
        raise Http404()
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
    return  HttpResponseRedirect('play')

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

@api_view(['GET'])
def current_user(request):
    user = request.user
    username = user.get_username()
    # TODO: error try/catch
    char = Character.objects.get(user=user)
    char_name = char.name
    char_description = char.description
    room_name = char.room.name
    portals_available = Portal.objects.filter(entry=char.room)
    directions_available = [portal_available.direction for portal_available in portals_available if portal_available.is_enable]
    tmp = 'game/api/' + char_name + '/move/'
    dic = {}
    for direction_available in directions_available:
        dic[direction_available] = tmp + direction_available
    return Response({
        'username': username,
        'charname': char_name,
        'chardescription': char_description,
        'roomname': room_name,
        'directions': dic
    })

@api_view(['PUT'])
def move_char_to_direction(request, char_name, direction):
    char = Character.objects.get(name = char_name)
    char.move(direction)
    char.save()
    portals_available = Portal.objects.filter(entry=char.room)
    directions_available = [portal_available.direction for portal_available in portals_available if portal_available.is_enable]
    tmp = 'game/api/' + char_name + '/move/'
    dic = {}
    for direction_available in directions_available:
        dic[direction_available] = tmp + direction_available
    return Response({
        'username': char.user.username,
        'charname': char_name,
        'chardescription': char.description,
        'roomname': char.room.name,
        'directions': dic
    })

class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()

#@login_required
def CreateCharacter(request):
    if request.method == 'POST':
        form = NewCharacterFrom(request.POST, request.FILES)
        print('form.is_valid', form.is_valid())
        if form.is_valid():
            character = Character()
            character.user = request.user
            character.name = form.cleaned_data['name']
            character.description = form.cleaned_data['description']
            character.avatar = form.cleaned_data['avatar']
            character.room = Room.objects.get(name='1')
            character.save()
            # print('redirecting....')
            return HttpResponseRedirect('play')
            # http://stackoverflow.com/questions/11241668/what-is-reverse-in-django
    else:
        form = NewCharacterFrom()

    return render(request, 'createcharacter.html', locals())