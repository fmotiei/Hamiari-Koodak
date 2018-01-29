from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse


# Create your views here.
import karbar
from madadju.models import Madadju, Niaz


def show_afzoudan_niaz(request):
    template = 'madadkar/afzoudan_niaz.html'
    return render(request, template, {})

def show_madadkar(request):
    template = 'karbar/index.html'
    return render(request, template, {'tozihat': karbar.darbare_ma.tozihat_text()
        , 'images': karbar.darbare_ma.akhbar_image()
        , 'progress': karbar.darbare_ma.progress()
        , 'utype': 'madadkar'})


def show_afzayesh_etebar(request):
    template = 'madadkar/afzayesh_etebar.html'
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


def show_moshahede_madadjuyan_dar_entezar_madadkar(request):
    template = 'madadkar/moshahede_madadjuyan_dar_entezar_madadkar.html'
    return render(request, template, {})


def show_profile_madadju_bi_kefalat(request):
    template = 'madadkar/profile_madadju_bi_kefalat.html'
    return render(request, template, {})

def show_niaz_haye_madadju_bi_kefalat(request):
    template = 'madadkar/niaz_haye_madadju_bi_kefalat.html'
    return render(request, template, {})

def show_ahdaf(request):
    template = 'karbar/ahdaf.html'
    return render(request, template, {'ahdaf': karbar.darbare_ma.ahdaf_text()
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : 'madadkar'})


def show_ashnai(request):
    template = 'karbar/ashnai.html'
    return render(request, template, {'ashnai': karbar.darbare_ma.ashnai_text()
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : 'madadkar'})


def show_sakhtar_sazmani(request):
    template = 'karbar/sakhtar_sazmani.html'
    return render(request, template, {'sakhtar_sazmani': karbar.darbare_ma.sakhtar_sazmani_text()
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : 'madadkar'})

def show_moshahede_list_koodakan(request):
    template = 'karbar/moshahede_list_koodakan.html'
    madadjuyan = Madadju.objects.all()
    return render(request, template, {'madadjuyan':[(m.first_name,Niaz.objects.filter(niazmand=m),Niaz.niaz_taminnashode(m)) for m in madadjuyan]
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : 'madadkar'})

def show_moshahede_list_niazhaye_fori_taminnashode(request):
    template = 'karbar/moshahede_list_niazhaye_fori_taminnashode.html'
    madadjuyan = Madadju.objects.all()
    return render(request, template, {'madadjuyan':[( m.first_name, ((niaz.onvan,niaz.mablagh_taminnashode()) for niaz in Niaz.niaz_taminnashode(m).filter(niazFori=True))) for m in madadjuyan]
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : 'madadkar'})