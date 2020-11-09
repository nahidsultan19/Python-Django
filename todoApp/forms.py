from django import forms
from django.forms import ModelForm

from .models import *

class todoItemForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add New Items...'}))
    class Meta:
        model = todoItem
        fields = '__all__'
