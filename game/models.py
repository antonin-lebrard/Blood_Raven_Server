from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models import Q

class Room(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self): # in Python3 need to be str (not unicode) for admin interface
        return self.name

class Character(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50, blank=True)
    room = models.ForeignKey(Room)

    def moove(self, direction):
        portal = Portal.objects.get(Q(entry=self.room) and Q(direction=direction))
        if not portal:
            pass
        else:
            if not portal.is_enable:
                pass
            else:
                self.room = portal.exit

    def __str__(self):
        return self.name

class Portal(models.Model):
    is_enable = models.BooleanField(default=True)
    NORD = 'N'
    SUD = 'S'
    EST = 'E'
    WEST = 'W'
    DIRECTION_CHOICES = (
        (NORD, 'North'),
        (SUD, 'South'),
        (EST, 'East'),
        (WEST, 'West'),
    )
    direction = models.CharField(max_length=1, choices=DIRECTION_CHOICES)
    entry = models.ForeignKey(Room, related_name='portal_entry')
    exit = models.ForeignKey(Room, related_name='portal_exit')

    def __str__(self):
        return self.entry.name + '->' + self.exit.name + ' (' + self.direction + ')'