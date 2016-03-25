# Create your tests here.

from .models import Character, Room, Portal
from django.contrib.auth.models import User

# Users
u1 = User.objects.create_superuser(username='rernande', email='trash@gmail.com', password='rernande') #Attention get_or_create
u2 = User.objects.create_user(username='antonin', password='antonin')

# Rooms
r1 = Room(name='1')
r1.save()
r2 = Room(name='2')
r2.save()
r3 = Room(name='3')
r3.save()

# Characters
c1 = Character(name='Conan', room=r1, user=u1)
c1.save()

# Portals
p1 = Portal(direction='N', entry=r1, exit=r2)
p1.save()
p2 = Portal(direction='E', entry=r2, exit=r3)
p2.save()