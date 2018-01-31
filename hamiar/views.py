from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse


# Create your views here.
import karbar
from madadju.models import Madadju, Niaz


def show_hamiar(request):
    template = 'karbar/index.html'
    return render(request, template, {'tozihat': karbar.darbare_ma.tozihat_text()
        , 'images': karbar.darbare_ma.akhbar_image()
        , 'progress': karbar.darbare_ma.progress()
        , 'utype': 'hamiar'})


def show_afzayesh_etebar(request):
    template = 'karbar/afzayesh_etebar.html'
    return render(request, template, {'utype' : 'madadju'
                                   , 'progress': karbar.darbare_ma.progress()})


def show_ersal_payam(request):
    template = 'karbar/ersal_payam.html'
    return render(request, template, {'utype' : 'madadju'
                                   , 'progress': karbar.darbare_ma.progress()})


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



def show_niaz_haye_madadju(request):
    template = 'hamiar/niaz_haye_madadju.html'
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

def show_profile_madadju(request):
    template = 'hamiar/profile_madadju.html'
    return render(request, template, {})

def show_roydad_ha(request):
    template = 'hamiar/roydad_ha.html'
    return render(request, template, {})


def show_sandoghe_payamhaye_daryafti(request):
    template = 'hamiar/sandoghe_payamhaye_daryafti.html'
    return render(request, template, {})


def show_sandoghe_payamhaye_ersali(request):
    template = 'hamiar/sandoghe_payamhaye_ersali.html'
    return render(request, template, {})


def show_amaliat_movafagh(request):
    template = 'karbar/amaliat_movafagh.html'
    return render(request, template, {'utype' : 'madadju'
                                      , 'progress': karbar.darbare_ma.progress()})

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