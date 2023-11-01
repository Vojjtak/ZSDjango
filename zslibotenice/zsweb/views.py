from django.shortcuts import render
from .models import Aktualita


def index(request):
    return render(request, "nase_skola/index.html")


def aktuality(request):
    aktuality_list = Aktualita.objects.all()
    return render(request, "nase_skola/aktuality.html",
                  {'aktuality_list': aktuality_list})


def organizaceskoly(request):
    return render(request, "nase_skola/organizace_skol.html")


def organizaceroku(request):
    return render(request, "nase_skola/organizace_skol_roku.html")


def zapisprvnitrida(request):
    return render(request, "nase_skola/zapis_prvni_trida.html")


def poradny(request):
    return render(request, "nase_skola/poradny.html")


def zamestnanci(request):
    return render(request, "nase_skola/zamestnanci.html")


def dokumenty(request):
    return render(request, "nase_skola/dokumenty.html")


def historie(request):
    return render(request, "nase_skola/historie.html")


def projekty(request):
    return render(request, "nase_skola/projekty.html")


def dokumenty_ms(request):
    return render(request, "materska_skolka/dokumenty_ms.html")


def ms(request):
    return render(request, "materska_skolka/ms.html")


def projekty_ms(request):
    return render(request, "materska_skolka/projekty_ms.html")


def zapis_ms(request):
    return render(request, "materska_skolka/zapis_ms.html")


def jidelna(request):
    return render(request, "jidelna/jidelna.html")

def kontakt(request):
    return render(request, "kontakt/kontakt.html")
