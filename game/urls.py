from Blood_Raven_Server import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from game.views import play, login_view, logout_view, RoomViewSet, CharacterViewSet, current_user, UserViewSet, move_char_to_direction
from rest_framework import routers
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'character', CharacterViewSet)
router.register(r'room', RoomViewSet)
router.register(r'room', UserViewSet)

urlpatterns = [
    url(r'^play', TemplateView.as_view(template_name="index.html")),
    #url(r'^play', play, name='play'),
    url(r'^login', login_view, name='login'),
    url(r'^logout', logout_view, name='logout'),
    #url(r'^register', play, name='register'),
    #url(r'^createcharacter', play, name='createcharacter'),
    url(r'^api/character/(?P<char_name>\w{1,50})/move/(?P<direction>\w{1})$', move_char_to_direction),
    url(r'^api/user/current', current_user, name='current_user'),
    url(r'^api/', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)