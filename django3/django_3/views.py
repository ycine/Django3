from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Model1Form
from .models import Model1
# Create your views here.


def strona_glowna(request):
    return HttpResponse("<h1>Witam !</h1>")


# def szablon(request):
#     model1form = Model1Form(request.POST or None)
#     if model1form.is_valid():
#         print(request.POST)
#         print(model1form.cleaned_data)
#         # imie = model1form.cleaned_data['imie']
#         # print(imie)
#         obj = Model1.objects.create(**model1form.cleaned_data)
#         # print(obj)
#         obj.save()

#     return render(request, "szablon.html")


def szablon(request, id=0):
    if request.method == "GET":
        if id==0:
            obiekt = Model1Form()
        else:
            insta = Model1.objects.get(id=id)
            obiekt = Model1Form(instance=insta)
        return render(request, "szablon.html", {'obiekt':obiekt})

    else:
        if id == 0:
            obiekt = Model1Form(request.POST)
            ob = {"form":obiekt}
        else:
            insta = Model1.objects.get(id=id)
            obiekt = Model1Form(request.POST, instance=insta)

            
        if obiekt.is_valid():
            # obj = Model1.objects.create(**model1form.cleaned_data)
            obiekt.save()
            # return HttpResponse("data submitted successfully") 
        else:
            
            html = 'we have recieved this form again'
            return render(request, 'szablon.html', {'obiekt':obiekt})
            # return HttpResponse(ob) 

        return redirect('/szablon_get')



def szablon_get(request):
    #TO ZWROCI POJEDYNCZY OBIEKT Z BAZY Z DANYM ID
    obj = Model1.objects.get(id=3)
    context = {
        'numer':obj.numer,
        'imie':obj.imie,
        'nazwisko': obj.nazwisko,
        'email': obj.email,
        # 'obiekty': Model1.objects.all()
    }
    

    obj2 = Model1.objects.all()
    context2 = {'obiekty': obj2}
    
    return render(request, "model1/model1_get.html", context2)


def szablon_delete(request, id):
   obiekt = Model1.objects.get(id=id)
   obiekt.delete()
   return redirect( "/szablon_get")



# def szablon_update(request, id):
#    obiekt = Model1.objects.get(id=id)
#    model1form = Model1Form(request.POST or None, instance=obiekt)
# #    if model1form.is_valid():   
#     #    obj = Model1.objects.create(**model1form.cleaned_data)
#     #    obj.save()

#    return render(request, "szablon.html", {'model1form':model1form, 'obiekt':obiekt})