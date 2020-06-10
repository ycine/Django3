from django.http import HttpResponse
from django.shortcuts import render
# from .formularz1 import formularz


def strona_glowna(request):
    return HttpResponse("<h1>Witam !</h1>")


def kontakt(request):
    return HttpResponse("<h1>Zadzwoń ! koniecznie !</h1>"
                        "<h2>0 - 700 - 888 - 888</h2>")


def o_stronie(request):
    formu = formularz(request.POST or None)
    return HttpResponse("<h1>Taka nowa!</h1>")


def szablon(request):
    val1 = request.POST.get('id')
    val2 = request.POST.get('imie')
    val3 = request.POST.get('nazwisko')
    val4 = request.POST.get('email')
    return render(request, "szablon.html")


def add(request):

    val1 = request.GET['numer1']
    val2 = request.GET['numer2']
    val3 = request.GET['numer3']
    resul = val1 + val2 + val3
    return render(request, "szablon-wynik.html", {'result': resul})

def szablon1(request):
    return render(request, "index.html")
