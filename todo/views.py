from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


# Create your views here.
def get_todo_list(request):
    items = Item.objects.all()  # query set of all items in the db
    context = {        # dict with items
        'items': items

    } 
    return render(request, 'todo/todo_list.html', context)  #  add context as arg so can be accessed in todo_list.html template


def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)  # populate form in django with request.POST data instead of doing it manually
        if form.is_valid():   # is_valid= django compare data in post request to data required on model
            form.save()        # see commits for original code

        return redirect('get_todo_list')  #directed here after adding item
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)
        
    
    