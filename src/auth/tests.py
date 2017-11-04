from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.authtoken.models import Token

# Create your tests here.
user1 = User.objects.get(id=1)
print user1
token = Token.objects.create(user=user1)
print token.key