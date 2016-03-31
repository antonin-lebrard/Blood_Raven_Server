from django.conf.urls import url, include
from game.views import play, login_view, logout_view, RoomViewSet, CharacterViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'character', CharacterViewSet)
router.register(r'room', RoomViewSet)

urlpatterns = [
    url(r'^play', play, name='play'),
    url(r'^login', login_view, name='login'),
    url(r'^logout', logout_view, name='logout'),
    url(r'^register', play, name='register'),
    url(r'^createcharacter', play, name='createcharacter'),
    url(r'^api/', include(router.urls)),
]