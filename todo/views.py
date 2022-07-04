from django.shortcuts import render, HttpResponse
from .models import Item


# Create your views here.
def get_todo_list(request):
    items = Item.objects.all()  #query set of all items in the db
    context = {        # dict with items
        'items': items

    } 
    return render(request, 'todo/todo_list.html', context)  #  add context as arg so can be accessed in todo_list.html template
    