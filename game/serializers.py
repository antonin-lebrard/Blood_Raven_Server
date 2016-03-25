from rest_framework import serializers
from game.models import Character, Room

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ('name', 'room', )

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('name', )