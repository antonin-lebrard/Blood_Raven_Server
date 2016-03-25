from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models import Q

class Room(models.Model):
    name = models.CharField(max_length=20)

class Character(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=20)
    room = models.ForeignKey(Room)

    def moove(self, direction):
        portal = Portal.objects.filter(Q(entry=self.room) and Q(direction=direction))[0]
        if not portal:
            pass
        else:
            if not portal.is_enable:
                pass
            else:
                self.room = portal.exit

class Portal(models.Model):
    is_enable = models.BooleanField(default=True)
    direction = models.CharField(max_length=1)
    entry = models.ForeignKey(Room, related_name='portal_entry')
    exit = models.ForeignKey(Room, related_name='portal_exit')