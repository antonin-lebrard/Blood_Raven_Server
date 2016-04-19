from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models import Q

class Room(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self): # in Python3 need to be str (not unicode) for admin interface
        return self.name

class Character(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=50, blank=True)
    room = models.ForeignKey(Room)
    avatar = models.ImageField(upload_to='img')

    def move(self, direction):
        portal = Portal.objects.get(Q(entry=self.room) and Q(direction=direction))
        if not portal:
            print('no portal')
            pass
        else:
            if not portal.is_enable:
                print('not enable')
                pass
            else:
                self.room = portal.exit
                return (self.name + ' has been moved to room ' + self.room.name)

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