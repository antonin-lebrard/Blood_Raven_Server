from django.conf.urls import url
from .views import play, login_view, logout_view
#from rest_framework import routers
#router = routers.DefaultRouter()
#router.register(r'character', CharacterViewSet)
#router.register(r'room', RoomViewSet)

urlpatterns = [
    url(r'^play', play),
    url(r'^login', login_view),
    url(r'^logout', logout_view),
    #url(r'^createcharacter$', views.home),
    #url(r'^api/', include(router.urls)),
]