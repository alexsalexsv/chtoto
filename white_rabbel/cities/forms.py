from django import forms
from .models import City


class CityForm(forms.ModelForm):
    name = forms.CharField(label='Город', widget=forms.TextInput(attrs={'class': 'form-control',
                           'placeholder': 'Введите город'}))
    img = forms.ImageField(label="Загрузить фотографию")

    class Meta:
        model = City
        fields = ('name', 'content', 'img')
        widgets = {
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
