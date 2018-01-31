from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse


# Create your views here.
import karbar
from madadju.models import Madadju, Niaz


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
    template = 'karbar/index.html'
    return render(request, template, {'tozihat': karbar.darbare_ma.tozihat_text()
        , 'images': karbar.darbare_ma.akhbar_image()
        , 'progress': karbar.darbare_ma.progress()
        , 'utype': 'modir'})


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


def show_madadjuyan(request):
    template = 'modir/madadjuyan.html'
    return render(request, template, {})

def show_payam_daryafti(request):
    template = 'modir/payam_daryafti.html'
    return render(request, template, {})


def show_profile(request):
    template = 'modir/profile.html'
    return render(request, template, {})


def show_roydad_ha(request):
    template = 'modir/roydad_ha.html'
    return render(request, template, {})


def show_sabtnam_madadkar(request):
    template = 'modir/sabtnam.html'
    return render(request, template, {})


def show_sabtename_modir_karshenas(request):
    template = 'modir/sabtename_modir_karshenas.html'
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

def show_moshahede_tarakoneshe_mali_karbar(request):
    template = 'modir/moshahede_tarakoneshe_mali_karbar.html'
    return render(request, template, {})

def show_afzayesh_etebar(request):
    template = 'karbar/afzayesh_etebar.html'
    return render(request, template, {})

def show_afzayesh_etebar(request):
    template = 'modir/afzayesh_etebar.html'
    return render(request, template, {})

def show_madadju_profile(request):
    template = 'modir/madadju_profile.html'
    return render(request, template, {})

def show_ahdaf(request):
    template = 'karbar/ahdaf.html'
    return render(request, template, {'ahdaf': karbar.darbare_ma.ahdaf_text()
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : 'modir'})


def show_ashnai(request):
    template = 'karbar/ashnai.html'
    return render(request, template, {'ashnai': karbar.darbare_ma.ashnai_text()
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : 'modir'})


def show_sakhtar_sazmani(request):
    template = 'karbar/sakhtar_sazmani.html'
    return render(request, template, {'sakhtar_sazmani': karbar.darbare_ma.sakhtar_sazmani_text()
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : 'modir'})

def show_moshahede_list_koodakan(request):
    template = 'karbar/moshahede_list_koodakan.html'
    madadjuyan = Madadju.objects.all()
    return render(request, template, {'madadjuyan':[(m.first_name,Niaz.objects.filter(niazmand=m),Niaz.niaz_taminnashode(m)) for m in madadjuyan]
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : 'modir'})

def show_moshahede_list_niazhaye_fori_taminnashode(request):
    template = 'karbar/moshahede_list_niazhaye_fori_taminnashode.html'
    madadjuyan = Madadju.objects.all()
    return render(request, template, {'madadjuyan':[( m.first_name, ((niaz.onvan,niaz.mablagh_taminnashode()) for niaz in Niaz.niaz_taminnashode(m).filter(niazFori=True))) for m in madadjuyan]
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : 'modir'})