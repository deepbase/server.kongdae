from django.test import TestCase
from musics.data.Composer import getComposers

# Create your tests here.
composers = getComposers()
# print composers
# print [item for item in composers]

# COMPOSERS = [item for item in composers]

COMPOSERS = [(item, getComposers()[item][1]) for item in getComposers()]

# ttt = [(item, composers[item][1]) for item in COMPOSERS]

for i in COMPOSERS :
    print(i[1])