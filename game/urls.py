from django.conf.urls import url, include
from game.views import login_view, logout_view, RoomViewSet, CharacterViewSet, current_user, UserViewSet, move_char_to_direction, play2, CreateCharacter
from rest_framework import routers
from django.views.generic import TemplateView
from django.conf.urls.static import static
from Blood_Raven_Server import settings
from django.contrib.auth.decorators import login_required

router = routers.DefaultRouter()
router.register(r'character', CharacterViewSet)
router.register(r'room', RoomViewSet)
router.register(r'room', UserViewSet) #TODO: WTF

urlpatterns = [
    url(r'^play2', play2, name='play2'),
    url(r'^play', login_required(TemplateView.as_view(template_name="index.html")), name='play'),
    url(r'style.css', TemplateView.as_view(template_name="style.css"), name='style.css'),
    url(r'main.dart.js', TemplateView.as_view(template_name="main.dart.js"), name='main.dart.js'),
    url(r'^login', login_view, name='login'),
    url(r'^logout', logout_view, name='logout'),
    url(r'^createcharacter', CreateCharacter, name='createcharacter'),
    url(r'^api/move/(?P<direction>\w{1})$', move_char_to_direction),
    url(r'^api/user/current', current_user, name='current_user'),
    url(r'^api/', include(router.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
