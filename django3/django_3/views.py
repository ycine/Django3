from django.shortcuts import render
from django.http import HttpResponse
from .forms import Model1Form
from .models import Model1
# Create your views here.


def strona_glowna(request):
    return HttpResponse("<h1>Witam !</h1>")


def szablon(request):
    model1form = Model1Form(request.POST or None)
    if model1form.is_valid():
        print(request.POST)
        print(model1form.cleaned_data)
        imie = model1form.cleaned_data['imie']
        obj = Model1.objects.create(**model1form.cleaned_data)



        # obj = Model1Form()
        # obj.imie = imie
        # obj.save()

        # model1form = Model1Form()
    return render(request, "szablon.html")