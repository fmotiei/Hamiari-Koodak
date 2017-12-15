from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse


# Create your views here.

def show_hamiar(request):
    template = 'hamiar/hamiar.html'
    return render(request, template, {})


def show_afzayesh_etebar(request):
    template = 'hamiar/afzayesh_etebar.html'
    return render(request, template, {})


def show_ahdaf(request):
    template = 'hamiar/ahdaf.html'
    return render(request, template, {})


def show_ashnai(request):
    template = 'hamiar/ashnai.html'
    return render(request, template, {})


def show_ersal_payam(request):
    template = 'hamiar/ersal_payam.html'
    return render(request, template, {})


def show_hemayat_az_moasese(request):
    template = 'hamiar/hemayat_az_moasese.html'
    return render(request, template, {})


def show_hemayat_az_niaz(request):
    template = 'hamiar/hemayat_az_niaz.html'
    return render(request, template, {})


def show_moshahede_niaz_haye_taht_hemayat(request):
    template = 'hamiar/moshahede_niaz_haye_taht_hemayat.html'
    return render(request, template, {})


def show_moshahede_tarakonesh_haye_mali(request):
    template = 'hamiar/moshahede_tarakonesh_haye_mali.html'
    return render(request, template, {})


def show_niaz_haye_tamin_nashode(request):
    template = 'hamiar/niaz_haye_tamin_nashode.html'
    return render(request, template, {})


def show_niaz_haye_tamin_nashode_fori(request):
    template = 'hamiar/niaz_haye_tamin_nashode_fori.html'
    return render(request, template, {})


def show_payam_daryafti(request):
    template = 'hamiar/payam_daryafti.html'
    return render(request, template, {})


def show_payam_ersali(request):
    template = 'hamiar/payam_ersali.html'
    return render(request, template, {})


def show_profile(request):
    template = 'hamiar/profile.html'
    return render(request, template, {})


def show_roydad_ha(request):
    template = 'hamiar/roydad_ha.html'
    return render(request, template, {})


def show_sakhtar_sazmani(request):
    template = 'hamiar/sakhtar_sazmani.html'
    return render(request, template, {})


def show_sandoghe_payamhaye_daryafti(request):
    template = 'hamiar/sandoghe_payamhaye_daryafti.html'
    return render(request, template, {})


def show_sandoghe_payamhaye_ersali(request):
    template = 'hamiar/sandoghe_payamhaye_ersali.html'
    return render(request, template, {})


def show_amaliat_movafagh(request):
    template = 'hamiar/amaliat_movafagh.html'
    return render(request, template, {})
