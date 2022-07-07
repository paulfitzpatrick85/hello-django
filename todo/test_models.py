from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    #  check that todo items are create with default status of false
    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)
