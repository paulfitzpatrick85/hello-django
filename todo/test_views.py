from django.test import TestCase

# Create your tests here.

class TestDjango(TestCase):
    def test_this_thing_works(self):  #self refers to test django class 
        self.assertEqual(1, 1)  # compare/check if 1 == 0

