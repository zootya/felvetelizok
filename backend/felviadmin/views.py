from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Szak, Felvetelizo
from .forms import SzakForm, FelvetelizoForm

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


def ujAdatForm(request):
    if request.method == "GET":
        form = FelvetelizoForm()
        return render(request, "ujadat_form.html", {"urlapAdat" : form })
    elif request.method == "POST":
        form = FelvetelizoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            #return HttpResponse('<h1> Hoppsz! Ez nem sikerült próbáld újra !</h1>')
            message = "Az adatok nem felelnek meg, nincs tárolás !"
            return render(request, "data-error.html", {"error_message" : message })


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
    
def ujSzakWeblap(request):
    szakok = Szak.objects.all().order_by("szakNev")
    context = {"szakok": szakok}
    return render(request, "ujszak.html", context)


def ujSzakForm(request):
    if request.method == "GET":
        form = SzakForm()
        return render(request, "ujszak_form.html", {"urlapSzak" : form })
    elif request.method == "POST":
        form = SzakForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            message = "Az adatok nem felelnek meg, nincs tárolás !"
            return render(request, "data-error", {"error_message" : message })

def ujSzakRogzit(request):
    _nev = request.POST.get('ujSzakNev')
    _tamogatott = request.POST.get('ujSzakkoltseg') == "on"        
    if len(_nev) > 0 :
        ujszak = Szak(
            szakNev = _nev, 
            tamogatott = _tamogatott,
        )
        ujszak.save()
    return redirect("../felviadmin/")

def modositAdat(request, itemId):
    osszesAdat = Felvetelizo.objects.all().order_by("nev")
    context = {
               "modositando": Felvetelizo.objects.get(id = itemId),
               "szakok": Szak.objects.all().order_by("szakNev"),
               }
    return render(request, "modositas.html", context)

def modositRogzit(request):
    if request.method == "POST":
        _id =  request.POST['modositId']
        _nev = request.POST['modositNev']
        _szul_evszam = request.POST['modositSzul_evszam']
        _pontszam = request.POST['modositPontszam']
        _szak_id = request.POST['modositSzak']
        _szak = Szak.objects.get(pk = _szak_id)
        
        if len(_nev) > 0 and _szul_evszam.isnumeric() and _pontszam.isnumeric() :
            modositando = Felvetelizo.objects.get(id = _id)
            modositando.nev = _nev 
            modositando.szul_evszam = _szul_evszam
            modositando.pontszam = _pontszam
            modositando.szak = _szak
            modositando.save()

        return redirect("../felviadmin/")
        #return redirect("index")


def feladat_views(request):
    return render(request, "feladat.html")


def dataError(request):
    message = "Itt a bibi !"
    return render(request, "data-error.html", {"error_message" : message })

def kapcsolat(request):
    adatok = {
        "nev" : "Kardos Zoltán",
        "email" : "level kardos zoltannak kukac gmail pont kom",
    }
    return render(request, "kapcsolat.html", {"kapcsolatiAdatok" : adatok })