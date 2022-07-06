from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    
    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})   # simulate form not filled out
        self.assertFalse(form.is_valid())   #  ensure form not valid
        self.assertIn('name', form.errors.keys())  # return dict of fields where errors were
        self.assertEqual(form.errors['name'][0], 'This field is required.')  # check that error in field is ...

    # def test_done_field_is_not_required(self):  # not required = defaulted to falsein item model
    #     form = ItemForm({'name', 'Test Todo Item'})  # should be valid with just name details
    #     self.assertTrue(form.is_valid())  

    # will stop info being shown unintentionally, stops fields being re-ordered
    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])