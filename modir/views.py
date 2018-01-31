from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse


# Create your views here.
import karbar
from karbar import moshtarak
from madadju.models import Madadju, Niaz


def show_ezafe_kardan_amr_kheyrie_motefareghe(request):
    template = 'modir/ezafe_kardan_amr_kheyrie_motefareghe.html'
    return render(request, template, {})


def show_list_omur_kheyrie(request):
    template = 'modir/list_omur_kheyrie.html'
    return render(request, template, {})


def show_moshahede_etelat_mali_karbaran(request):
    template = 'modir/moshahede_etelat_mali_karbaran.html'
    return render(request, template, {})


def show_moshahede_hamyaran_dar_entezar_taeid(request):
    template = 'modir/moshahede_hamyaran_dar_entezar_taeid.html'
    return render(request, template, {})

def show_moshahede_madadjuyan_dar_entezar_madadkar(request):
    template = 'modir/moshahede_madadjuyan_dar_entezar_madadkar.html'
    return render(request, template, {})


def show_madadjuyan(request):
    template = 'modir/madadjuyan.html'
    return render(request, template, {})

def show_profile(request):
    template = 'modir/profile.html'
    return render(request, template, {})

def show_sabtnam_madadkar(request):
    template = 'modir/sabtnam.html'
    return render(request, template, {})


def show_sabtename_modir_karshenas(request):
    template = 'modir/sabtename_modir_karshenas.html'
    return render(request, template, {})

def show_moshahede_tarakoneshe_mali_karbar(request):
    template = 'modir/moshahede_tarakoneshe_mali_karbar.html'
    return render(request, template, {})

def show_madadju_profile(request):
    template = 'modir/madadju_profile.html'
    return render(request, template, {})



def show_modir(request):
    return moshtarak.show_user(request,'modir')


def show_afzayesh_etebar(request):
    return moshtarak.show_afzayesh_etebar(request,'modir')


def show_ersal_payam(request):
    return moshtarak.show_ersal_payam(request,'modir')

def show_moshahede_tarakonesh_haye_mali(request):
    return moshtarak.show_moshahede_tarakonesh_haye_mali(request,'modir')

def show_payam_daryafti(request):
    return moshtarak.show_payam_daryafti(request,'modir')

def show_payam_ersali(request):
    return moshtarak.show_payam_ersali(request,'modir')


def show_roydadha(request):
    return moshtarak.show_roydadha(request,'modir')


def show_sandoghe_payamhaye_daryafti(request):
    return moshtarak.show_sandoghe_payamhaye_daryafti(request,'modir')


def show_sandoghe_payamhaye_ersali(request):
    return moshtarak.show_sandoghe_payamhaye_ersali(request,'modir')


def show_amaliat_movafagh(request):
    return moshtarak.show_amaliat_movafagh(request,'modir')

def show_ahdaf(request):
    return moshtarak.show_ahdaf(request,'modir')

def show_ashnai(request):
    return moshtarak.show_ashnai(request,'modir')


def show_sakhtar_sazmani(request):
    return moshtarak.show_sakhtar_sazmani(request,'modir')

def show_moshahede_list_koodakan(request):
    return moshtarak.show_moshahede_list_koodakan(request,'modir')

def show_moshahede_list_niazhaye_fori_taminnashode(request):
    return moshtarak.show_moshahede_list_niazhaye_fori_taminnashode(request,'modir')