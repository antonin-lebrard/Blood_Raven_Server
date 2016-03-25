# Create your tests here.

from .models import Character, Room, Portal
from django.contrib.auth.models import User

# Rooms
r1 = Room()
r1.save()
r2 = Room()
r2.save()
r3 = Room()
r3.save()

# Users
u1 = User.objects.create_superuser(username='rernande', email='trash@gmail.com', password='rernande')
u2 = User.objects.create_user(username='antonin', password='antonin')

# Characters
c1 = Character(name='Conan', room=r1, user=u1)
c1.save()

# Portals

p1 = Portal(direction='N', entry=r1, exit=r2)
p1.save()
p2 = Portal(direction='E', entry=r2, exit=r3)
p2.save()