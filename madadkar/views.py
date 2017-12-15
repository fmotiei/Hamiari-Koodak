from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse


# Create your views here.


def show_afzoudan_niaz(request):
    template = 'madadkar/afzoudan_niaz.html'
    return render(request, template, {})

def show_madadkar(request):
    template = 'madadkar/madadkar.html'
    return render(request, template, {})


def show_afzayesh_etebar(request):
    template = 'madadkar/afzayesh_etebar.html'
    return render(request, template, {})


def show_ahdaf(request):
    template = 'madadkar/ahdaf.html'
    return render(request, template, {})


def show_ashnai(request):
    template = 'madadkar/ashnai.html'
    return render(request, template, {})


def show_ersal_payam(request):
    template = 'madadkar/ersal_payam.html'
    return render(request, template, {})

def show_moshahede_madadjuyan_taht_kefalat(request):
    template = 'madadkar/moshahede_madadjuyan_taht_kefalat.html'
    return render(request, template, {})


def show_moshahede_tarakonesh_haye_mali(request):
    template = 'madadkar/moshahede_tarakonesh_haye_mali.html'
    return render(request, template, {})


def show_niaz_haye_madadju(request):
    template = 'madadkar/niaz_haye_madadju.html'
    return render(request, template, {})

def show_niaz_haye_tamin_nashode(request):
    template = 'madadkar/niaz_haye_tamin_nashode.html'
    return render(request, template, {})


def show_niaz_haye_tamin_nashode_fori(request):
    template = 'madadkar/niaz_haye_tamin_nashode_fori.html'
    return render(request, template, {})


def show_payam_daryafti(request):
    template = 'madadkar/payam_daryafti.html'
    return render(request, template, {})


def show_payam_ersali(request):
    template = 'madadkar/payam_ersali.html'
    return render(request, template, {})


def show_payam_entezar(request):
    template = 'madadkar/payam_entezar.html'
    return render(request, template, {})


def show_profile(request):
    template = 'madadkar/profile.html'
    return render(request, template, {})


def show_profile_madadju(request):
    template = 'madadkar/profile_madadju.html'
    return render(request, template, {})


def show_roydad_ha(request):
    template = 'madadkar/roydad_ha.html'
    return render(request, template, {})


def show_sakhtar_sazmani(request):
    template = 'madadkar/sakhtar_sazmani.html'
    return render(request, template, {})


def show_sandoghe_payamhaye_daryafti(request):
    template = 'madadkar/sandoghe_payamhaye_daryafti.html'
    return render(request, template, {})


def show_sandoghe_payamhaye_ersali(request):
    template = 'madadkar/sandoghe_payamhaye_ersali.html'
    return render(request, template, {})


def show_sandoghe_payamhaye_entezar(request):
    template = 'madadkar/sandoghe_payamhaye_entezar.html'
    return render(request, template, {})


def show_sabte_naam_madadju(request):
    template = 'madadkar/sabte_naam_madadju.html'
    return render(request, template, {})


def show_amaliat_movafagh(request):
    template = 'madadkar/amaliat_movafagh.html'
    return render(request, template, {})


def show_virayesh_niaz(request):
    template = 'madadkar/virayesh_niaz.html'
    return render(request, template, {})


def show_vaziat_tahsili(request):
    template = 'madadkar/vaziat_tahsili.html'
    return render(request, template, {})
