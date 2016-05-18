from Blood_Raven_Server.forms import UserForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

def home(request):
    print(request.user)
    base_template = 'base.html' if not request.user == 'AnonymousUser' else 'base_logged.html'
    username = request.user.username or 'inconnu'
    return render(request, 'home.html', locals())

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return HttpResponseRedirect('game/login')
    else:
        form = UserForm()
    return render(request, 'register.html', locals())