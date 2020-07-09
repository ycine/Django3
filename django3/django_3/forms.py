from django import forms
from .models import Model1

class Model1Form(forms.ModelForm):
    class Meta:
        model = Model1
        fields = ['numer',
                'imie',
                'nazwisko',
                'email']
        # '__all__'


    def clean_numer(self):
        numer = self.cleaned_data.get('numer')
        numer2 = str(numer)
        if len(numer2) >= 19:
            raise forms.ValidationError("za dlugi")
        # TO MA SPRAWDZAC CZY JAK ISTNIEJE DANY OBIEKT W BAZIE TO ZWROCI BLAD
        for instance in Model1.objects.all():
            if instance.numer == numer:
                raise forms.ValidationError("obiekt o podajnej nazwie juz istnieje")
        
        else:
            return numer


    def clean_imie(self):
        imie = self.cleaned_data.get('imie')
        if len(imie) >= 19:
            raise forms.ValidationError("za dlugi")
        else:
            return imie


    def clean_nazwisko(self):
        nazwisko = self.cleaned_data.get('nazwisko')
        if len(nazwisko) < 19:
            return nazwisko
        else:
            raise forms.ValidationError("za dlugi")


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if len(email) < 19:
            return email
        else:
            raise forms.ValidationError("za dlugi")