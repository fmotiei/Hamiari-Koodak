from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse


# Create your views here.

def show_moshahede_list_koodakan(request):
    template = 'karbar/moshahede_list_koodakan.html'
    return render(request, template, {})

def show_moshahede_list_niazhaye_fori_taminnashode(request):
    template = 'karbar/moshahede_list_niazhaye_fori_taminnashode.html'
    return render(request, template, {})


def show_profile(request):
    template = 'karbar/profile.html'
    return render(request, template, {})


def show_sabtename_hamyar(request):
    template = 'karbar/sabtename_hamyar.html'
    return render(request, template, {})



def show_ahdaf(request):
    template = 'karbar/ahdaf.html'
    return render(request, template, {})


def show_ashnai(request):
    template = 'karbar/ashnai.html'
    return render(request, template, {})


def show_sakhtar_sazmani(request):
    template = 'karbar/sakhtar_sazmani.html'
    return render(request, template, {})
