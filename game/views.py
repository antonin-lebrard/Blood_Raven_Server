# Create your views here.

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Character
from game.forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect(home)# Redirect to a success page.
    return render(request, 'login.html', {'login_form': form })

@login_required
def home(request):
    user = request.user
    username = user.get_username()
    char = None
    room_id = None
    try:
        char = Character.objects.filter(Q(user=user))[0]
        char_name = char.name
        room_id = char.room.id
        # TODO: requete qui va chercher les directions dispo
    except Character.DoesNotExist:
        pass # redirect to createchar.html
    except Exception:
        pass # ne rien faire bien sur
    return render(request, 'home.html', locals())
    # redirect to /game/play (Anto)
    # qui effectue une requete /api/char_status
    # j'identifie de cette façon request.user.char et renvoie
    # {
    #   "name": "Conan",
	#   "room": "/api/room/room_id"
    # }

# class LogoutView(TemplateView):
#   template_name = 'logout.html'
#
#   def get(self, request, **kwargs):
#     logout(request)
#     return render(request, self.template_name)
#
# class CharacterViewSet(viewsets.ModelViewSet):
#     queryset = Character.objects.all()
#     serializer_class = CharacterSerializer
#
# class RoomViewSet(viewsets.ModelViewSet):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer


