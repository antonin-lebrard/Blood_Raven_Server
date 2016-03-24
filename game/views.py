# Create your views here.

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from game.forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect(home)# Redirect to a success page.
    return render(request, 'login.html', {'login_form': form })


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

#@login_required
def home(request):
    return render(request, 'home.html')

    #try:
    #    character = Character.objects.get(id=1)
    #except Character.DoesNotExist:
    #    raise Http404
    #return TemplateResponse(request, 'home.html', { 'character':character })