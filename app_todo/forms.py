from django import forms
from .models import Todos


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = ('title', 'description', 'start_time', 'end_time', 'status')