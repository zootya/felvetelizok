from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Szak, Felvetelizo
# Create your views here.

def index(request):
    osszesAdat = Felvetelizo.objects.all().order_by("nev")
    context = {"osszesAdat": osszesAdat}
    return render(request, "index.html", context)

def torolAdat(request, itemId):
    torlendo = Felvetelizo.objects.get(id = itemId)
    torlendo.delete()
    return redirect("../felviadmin/")

def ujAdatWeblap(request):
    szakok = Szak.objects.all().order_by("szakNev")
    context = {"szakok": szakok}
    return render(request, "ujadat.html", context)

def ujAdatRogzit(request):
    if request.method == "POST":
        _nev = request.POST['ujadatNev']
        _szul_evszam = request.POST['ujadatSzul_evszam']
        _pontszam = request.POST['ujadatPontszam']
        _szak_id = request.POST['ujadatSzak']
        _szak = Szak.objects.get(pk = _szak_id)
        
        if len(_nev) > 0 and _szul_evszam.isnumeric() and _pontszam.isnumeric() :
            ujadat = Felvetelizo(
                nev = _nev, 
                szul_evszam = _szul_evszam,
                pontszam = _pontszam,
                szak = _szak
                )
            ujadat.save()

        return redirect("../felviadmin/")            