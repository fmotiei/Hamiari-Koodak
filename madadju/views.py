from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse


# Create your views here.



def show_afzayesh_etebar(request):
    template = 'madadju/afzayesh_etebar.html'
    return render(request, template, {})


def show_ahdaf(request):
    template = 'madadju/ahdaf.html'
    return render(request, template, {})


def show_ashnai(request):
    template = 'madadju/ashnai.html'
    return render(request, template, {})


def show_darkhast_taghir_madadkar(request):
    template = 'madadju/darkhast_taghir_madadkar.html'
    return render(request, template, {})


def show_ersal_payam(request):
    template = 'madadju/ersal_payam.html'
    return render(request, template, {})


def show_madadju(request):
    template = 'madadju/madadju.html'
    return render(request, template, {})



def show_moshahede_tarakonesh_haye_mali(request):
    template = 'madadju/moshahede_tarakonesh_haye_mali.html'
    return render(request, template, {})


def show_payam_daryafti(request):
    template = 'madadju/payam_daryafti.html'
    return render(request, template, {})



def show_payam_ersali(request):
    template = 'madadju/payam_ersali.html'
    return render(request, template, {})


def show_profile(request):
    template = 'madadju/profile.html'
    return render(request, template, {})


def show_roydadha(request):
    template = 'madadju/roydadha.html'
    return render(request, template, {})


def show_sakhtar_sazmani(request):
    template = 'madadju/sakhtar_sazmani.html'
    return render(request, template, {})


def show_sandoghe_payamhaye_daryafti(request):
    template = 'madadju/sandoghe_payamhaye_daryafti.html'
    return render(request, template, {})


def show_sandoghe_payamhaye_ersali(request):
    template = 'madadju/sandoghe_payamhaye_ersali.html'
    return render(request, template, {})


def show_amaliat_movafagh(request):
    template = 'madadju/amaliat_movafagh.html'
    return render(request, template, {})
