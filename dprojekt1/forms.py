from django import forms


class Model1Form(forms.Form):
    id = forms.IntegerField()
    imie = forms.CharField()
    nazwisko = forms.CharField()
    email = forms.EmailField()
