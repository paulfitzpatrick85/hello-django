from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:  # inner class to give form data about itself
        model = Item
        fields = ['name', 'done']