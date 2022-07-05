from django.shortcuts import render, redirect
from .models import Item


# Create your views here.
def get_todo_list(request):
    items = Item.objects.all()  # query set of all items in the db
    context = {        # dict with items
        'items': items

    } 
    return render(request, 'todo/todo_list.html', context)  #  add context as arg so can be accessed in todo_list.html template


def add_item(request):
    if request.method == "POST":
        name = request.POST.get('item_name')  # the input in add_item.html
        done = 'done' in request.POST  # boolean value, check that checkbox is ticked basically
        Item.objects.create(name=name, done=done)  #create an item
        return redirect('get_todo_list')  #directed here after adding item

    return render(request, 'todo/add_item.html') 
        
    
    