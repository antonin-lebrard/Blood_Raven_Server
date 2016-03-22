from django.test import TestCase

# Create your tests here.

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eboutique.settings")

from django.db import models
from .models import Character, Room, Portal

# Rooms
r1 = Room()
r1.save()
r2 = Room()
r2.save()
r3 = Room()
r3.save()

# Characters
c1 = Character(name="Conan", room=r1)
c1.save()

# Portals

p1 = Portal(direction='N', entry=r1, exit=r2)
p1.save()
p2 = Portal(direction='E', entry=r2, exit=r3)
p2.save()