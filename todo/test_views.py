from django.test import TestCase
from .models import Item

# Create your tests here.


class TestViews(TestCase):

    # def test_this_thing_works(self):  #self refers to test django class 
    #     self.assertEqual(1, 1)  # compare/check if 1 == 0
    
    def test_get_todo_list(self):
        response = self.client.get('/')   # get homepage
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        response = self.client.get('/add')   # get homepage
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        item = Item.objects.create(name='Test Todo Item')   # item must be imported top of page to test
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        response = self.client.post('/add', {'name': 'Test Added Item'})   # name value as if we gave it a name
        self.assertRedirects(response, '/')  # redirect to homepage if added successfully

    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')   
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)  # test within test, try to retrieve id when it shouldn't exist anymore
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test Todo Item', done=True)   
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)  #get item again
        self.assertFalse(updated_item.done)  # check done status
