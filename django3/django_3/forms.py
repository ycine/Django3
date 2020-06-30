from django import forms
from .models import Model1

class Model1Form(forms.ModelForm):
    class Meta:
        model = Model1
        fields = '__all__'
    # numer = forms.IntegerField()
    # imie = forms.CharField()
    # nazwisko = forms.CharField()
    # email = forms.EmailField()
