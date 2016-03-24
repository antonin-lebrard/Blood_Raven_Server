from django.conf.urls import url
from .views import home, login_view
#from rest_framework import routers
#router = routers.DefaultRouter()
#router.register(r'character', CharacterViewSet)
#router.register(r'room', RoomViewSet)

urlpatterns = [
    url(r'^home$', home),
    url(r'^login$', login_view),
    #url(r'^logout$', LogoutView.as_view()),
    #url(r'^createcharacter$', views.home),
    #url(r'^api/', include(router.urls)),
]