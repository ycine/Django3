from django import forms


class Model1Form(forms.Form):
    numer = forms.IntegerField()
    imie = forms.CharField()
    nazwisko = forms.CharField()
    email = forms.EmailField()
