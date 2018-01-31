from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse
import karbar.darbare_ma

# Create your views here.
from karbar import moshtarak
from madadju.models import Madadju, Niaz

def show_profile(request):
    return moshtarak.show_user(request,'karbar')


def show_sabtename_hamyar(request):
    template = 'karbar/sabtename_hamyar.html'
    return render(request, template, {'progress':karbar.darbare_ma.progress()})
#TODO bayad vurudi bekhunim az html

def show_ahdaf(request):
    return moshtarak.show_ahdaf(request,'karbar')

def show_ashnai(request):
    return moshtarak.show_ashnai(request,'karbar')


def show_sakhtar_sazmani(request):
    return moshtarak.show_sakhtar_sazmani(request,'karbar')

def show_moshahede_list_koodakan(request):
    return moshtarak.show_moshahede_list_koodakan(request,'karbar')

def show_moshahede_list_niazhaye_fori_taminnashode(request):
    return moshtarak.show_moshahede_list_niazhaye_fori_taminnashode(request,'karbar')