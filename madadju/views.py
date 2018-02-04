from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse


# Create your views here.
import karbar
from karbar import moshtarak
from madadju.models import Madadju, Niaz


def show_darkhast_taghir_madadkar(request):
    template = 'madadju/darkhast.html'
    return render(request, template, {'utype' : 'madadju'
                                    , 'progress': karbar.darbare_ma.progress()
                                    ,'username' : ''
                                      , 'mName' : ''})
#TODO username : username karbar , mName : username madadkare marbute
#TODO tozihat ra begirad

def show_profile(request):
    template = 'madadju/profile.html'
    return render(request, template, {'utype' : 'madadju'
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : ''
                                    , 'first_name': ''
                                    , 'last_name': ''
                                    , 'alarm': ''
                                    , 'madadkar': ''
                                    , 'hamiarha': []})
#TODO username : username karbar , first_name : first name karbar , last_name : last name karbar , alarm : alarm karbar , madadkar : username madadkare marbute , hamiarha :username hamiaran marbute

def show_hamiar_profile(request):
    template = 'madadju/hamiar_profile.html'
    return render(request, template, {'utype' : 'madadju'
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : ''
                                      , 'husername' : ''
                                      , 'hfName' : ''
                                      , 'hlName' : ''
                                      , 'madadjuyan' : []})
#TODO username: username karbar , husername : username hamiar , hfName : first name hamiar , hlName : last name hamiar , madadjuyan : username madadjuyan tahte hemayat hamiar



def show_madadju(request):
    return moshtarak.show_user(request,'madadju')

def show_afzayesh_etebar(request):
    return moshtarak.show_afzayesh_etebar(request,'madadju')


def show_ersal_payam(request):
    return moshtarak.show_ersal_payam(request,'madadju')

def show_moshahede_tarakonesh_haye_mali(request):
    return moshtarak.show_moshahede_tarakonesh_haye_mali(request,'madadju')

def show_payam_daryafti(request):
    return moshtarak.show_payam_daryafti(request,'madadju')

def show_payam_ersali(request):
    return moshtarak.show_payam_ersali(request,'madadju')


def show_roydadha(request):
    return moshtarak.show_roydadha(request,'madadju')


def show_sandoghe_payamhaye_daryafti(request):
    return moshtarak.show_sandoghe_payamhaye_daryafti(request,'madadju')


def show_sandoghe_payamhaye_ersali(request):
    return moshtarak.show_sandoghe_payamhaye_ersali(request,'madadju')


def show_amaliat_movafagh(request):
    return moshtarak.show_amaliat_movafagh(request,'madadju')

def show_ahdaf(request):
    return moshtarak.show_ahdaf(request,'madadju')

def show_ashnai(request):
    return moshtarak.show_ashnai(request,'madadju')


def show_sakhtar_sazmani(request):
    return moshtarak.show_sakhtar_sazmani(request,'madadju')

def show_moshahede_list_koodakan(request):
    return moshtarak.show_moshahede_list_koodakan(request,'madadju')

def show_moshahede_list_niazhaye_fori_taminnashode(request):
    return moshtarak.show_moshahede_list_niazhaye_fori_taminnashode(request,'madadju')
