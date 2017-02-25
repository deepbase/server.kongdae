from django.test import TestCase
from musics.data.Composer import getComposers

# Create your tests here.
composers = getComposers()
print composers
print [item for item in composers]
print composers['Beethoven'][1]