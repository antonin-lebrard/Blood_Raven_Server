# Create your tests here.
import django
from django.db.models import Q

from django.test import TestCase
from game.models import Character, Portal, Room
from django.contrib.auth.models import User

# Users
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_superuser(username='rernande', email='trash@gmail.com',password='rernande')
        User.objects.create_user(username='antonin', password='antonin')

class RoomTestCase(TestCase):
    def setUp(self):
        Room.objects.create(name='1')
        Room.objects.create(name='2')
        Room.objects.create(name='3')

class PortalTestCase(TestCase):
    def setUp(self):
        Portal.objects.create(direction='N', entry=Room.objects.get(name='1'), exit=Room.objects.create(name='2'))
        Portal.objects.create(direction='E', entry=Room.objects.get(name='2'), exit=Room.objects.create(name='3'))

class CharacterTestCase(TestCase):
    def setUp(self):
        room1 = Room.objects.create(name='1')
        Portal.objects.create(direction='N', entry=room1, exit=Room.objects.create(name='2'))
        Character.objects.create(user=User.objects.create_superuser(username='rernande', email='trash@gmail.com',password='rernande'), name='Conan', description='Le barare', room=room1)

    def test_characters_can_moove(self):
        conan = Character.objects.get(name='Conan')
        self.assertEqual(conan.move('N'), 'Conan has been moved to room 2')