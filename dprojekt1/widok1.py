from django.http import HttpResponse
from django.shortcuts import render
from .forms import Model1Form


def strona_glowna(request):
    return HttpResponse("<h1>Witam !</h1>")


def kontakt(request):
    return HttpResponse("<h1>Zadzwoń ! koniecznie !</h1>"
                        "<h2>0 - 700 - 888 - 888</h2>")


def o_stronie(request):
    formu = formularz(request.POST or None)
    return HttpResponse("<h1>Taka nowa!</h1>")


def szablon(request):
    model1form = Model1Form(request.POST or None)
    if model1form.is_valid():
        print(request.POST)
        imie = model1form.cleaned_data['imie']
        obj = Model1Form.imie.create(**model1form.cleaned_data)
        model1form = Model1Form()
    return render(request, "szablon.html")


def add(request):

    val1 = request.GET['numer1']
    val2 = request.GET['numer2']
    val3 = request.GET['numer3']
    resul = val1 + val2 + val3
    return render(request, "szablon-wynik.html", {'result': resul})

def szablon1(request):
    return render(request, "index.html")
