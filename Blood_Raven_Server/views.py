from django.shortcuts import render

def home(request):
    username = request.user.username or 'inconnu'
    return render(request, 'home.html', locals())
