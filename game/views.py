from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse

from .models import Character
# Create your views here.

@login_required
def home(request):
    try:
        character = Character.objects.get(id=1)
    except Character.DoesNotExist:
        raise Http404
    return TemplateResponse(request, 'home.html', { 'character':character })
