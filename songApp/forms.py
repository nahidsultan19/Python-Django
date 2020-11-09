from django import forms
from .models import Songs

class SongsForm(forms.ModelForm):
    class Meta:
        model = Songs
        fields = '__all__'
        labels = {
            'title': 'Song Title'
        }

    def __init__(self, *args, **kwargs):
        super(SongsForm, self).__init__(*args, **kwargs)
        self.fields['band'].empty_label = 'Select'
        
