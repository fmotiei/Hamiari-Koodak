from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse


# Create your views here.

def show_ahdaf(request):
    template = 'modir/ahdaf.html'
    return render(request, template, {})


def show_ashnai(request):
    template = 'modir/ashnai.html'
    return render(request, template, {})


def show_ersal_payam(request):
    template = 'modir/ersal_payam.html'
    return render(request, template, {})


def show_ezafe_kardan_amr_kheyrie_motefareghe(request):
    template = 'modir/ezafe_kardan_amr_kheyrie_motefareghe.html'
    return render(request, template, {})


def show_list_omur_kheyrie(request):
    template = 'modir/list_omur_kheyrie.html'
    return render(request, template, {})


def show_modir(request):
    template = 'modir/modir.html'
    return render(request, template, {})


def show_moshahede_etelat_mali_karbaran(request):
    template = 'modir/moshahede_etelat_mali_karbaran.html'
    return render(request, template, {})


def show_moshahede_hamyaran_dar_entezar_taeid(request):
    template = 'modir/moshahede_hamyaran_dar_entezar_taeid.html'
    return render(request, template, {})


def show_moshahede_list_koodakan(request):
    template = 'modir/moshahede_list_koodakan.html'
    return render(request, template, {})


def show_moshahede_list_niazhaye_fori_taminnashode(request):
    template = 'modir/moshahede_list_niazhaye_fori_taminnashode.html'
    return render(request, template, {})


def show_moshahede_madadjuyan_dar_entezar_madadkar(request):
    template = 'modir/moshahede_madadjuyan_dar_entezar_madadkar.html'
    return render(request, template, {})


def show_payam_daryafti(request):
    template = 'modir/payam_daryafti.html'
    return render(request, template, {})


def show_profile(request):
    template = 'modir/profile.html'
    return render(request, template, {})


def show_roydadha(request):
    template = 'modir/roydadha.html'
    return render(request, template, {})


def show_sabtename_madadkar(request):
    template = 'modir/sabtename_madadkar.html'
    return render(request, template, {})


def show_sabtename_modir_karshenas(request):
    template = 'modir/sabtename_modir_karshenas.html'
    return render(request, template, {})


def show_sakhtar_sazmani(request):
    template = 'modir/sakhtar_sazmani.html'
    return render(request, template, {})


def show_sandoghe_payamhaye_daryafti(request):
    template = 'modir/sandoghe_payamhaye_daryafti.html'
    return render(request, template, {})


def show_sandoghe_payamhaye_ersali(request):
    template = 'modir/sandoghe_payamhaye_ersali.html'
    return render(request, template, {}
                )
def show_amaliat_movafagh(request):
    template = 'modir/amaliat_movafagh.html'
    return render(request, template, {})

def show_moshahede_tarakonesh_haye_mali(request):
    template = 'modir/moshahede_tarakonesh_haye_mali.html'
    return render(request, template, {})

def show_afzayesh_etebar(request):
    template = 'modir/afzayesh_etebar.html'
    return render(request, template, {})

def show_afzayesh_etebar(request):
    template = 'modir/afzayesh_etebar.html'
    return render(request, template, {})

def show_madadju_profile(request):
    template = 'modir/madadju_profile.html'
    return render(request, template, {})
