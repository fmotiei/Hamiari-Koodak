from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse


# Create your views here.
import karbar
from madadju.models import Madadju, Niaz


#TODO username befrestim

def show_darkhast_taghir_madadkar(request):
    template = 'madadju/darkhast.html'
    return render(request, template, {'utype' : 'madadju'
                                    , 'progress': karbar.darbare_ma.progress()
                                    ,'username' : ''})
#TODO html to DB
#TODO send madadju's madadkar name


def show_profile(request):
    template = 'madadju/profile.html'
    return render(request, template, {'utype' : 'madadju'
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : ''
                                    , 'first_name': ''
                                    , 'last_name': ''
                                    , 'alarm': '1'
                                    , 'madadkar': ''
                                    , 'hamiarha': {}})
#TODO vurudi takmil shavad

def show_afzayesh_etebar(request):
    template = 'karbar/afzayesh_etebar.html'
    return render(request, template, {'utype' : 'madadju'
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : ''})
#TODO html to DB


def show_ersal_payam(request):
    template = 'karbar/ersal_payam.html'
    return render(request, template, {'utype' : 'madadju'
                                   , 'progress': karbar.darbare_ma.progress()
                                      ,'username' : ''})


def show_madadju(request):
    template = 'karbar/index.html'
    return render(request, template, {'tozihat': karbar.darbare_ma.tozihat_text()
                                    , 'images': karbar.darbare_ma.akhbar_image()
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'utype': 'madadju'
                                    ,'username': ''})



def show_moshahede_tarakonesh_haye_mali(request):
    template = 'karbar/moshahede_tarakonesh_haye_mali.html'
    return render(request, template, {'utype' : 'madadju'
                                        , 'progress': karbar.darbare_ma.progress()
                                        , 'tarakoneshha' : {}
                                        ,'username': ''})
#TODO bayd tarakonesh haye mali ro behesh befrestim


def show_payam_daryafti(request):
    template = 'karbar/payam_daryafti.html'
    return render(request, template, {'utype' : 'madadju'
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username':''
                                    , 'onvan': ''
                                    , 'text' : ''
                                    , 'sender': ''
                                    , 'day': ''
                                    , 'hour' : ''})
#TODO onvan matne payam tarkh va fersatnde



def show_payam_ersali(request):
    template = 'karbar/payam_ersali.html'
    return render(request, template, {'utype': 'madadju'
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username': ''
                                    , 'onvan': ''
                                    , 'text': ''
                                    , 'sender': ''
                                    , 'day': ''
                                    , 'hour': ''})
#TODO onvan matne payam tarkh va fersatnde


def show_roydadha(request):
    template = 'karbar/roydadha.html'
    return render(request, template, {'utype' : 'madadju'
        , 'progress': karbar.darbare_ma.progress()
        , 'username':''
        , 'roydadha' : {} })
#TODO roydadha shamel onvan,text,day,hour


def show_sandoghe_payamhaye_daryafti(request):
    template = 'karbar/sandoghe_payamhaye_daryafti.html'
    return render(request, template, {'utype': 'madadju'
        , 'progress': karbar.darbare_ma.progress()
        , 'username': ''
        , 'payamha': {}})
#TODO payamha shamele sender,day,hour,onvan


def show_sandoghe_payamhaye_ersali(request):
    template = 'karbar/sandoghe_payamhaye_ersali.html'
    return render(request, template, {'utype': 'madadju'
        , 'progress': karbar.darbare_ma.progress()
        , 'username': ''
        , 'payamha': {}})
    # TODO payamha shamele receiver,day,hour,onvan


def show_amaliat_movafagh(request):
    template = 'karbar/amaliat_movafagh.html'
    return render(request, template, {'utype' : 'madadju'
                                      , 'progress': karbar.darbare_ma.progress()
                                      ,'username':''})

def show_ahdaf(request):
    template = 'karbar/ahdaf.html'
    return render(request, template, {'ahdaf': karbar.darbare_ma.ahdaf_text()
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : 'madadju'
                                      ,'username':''})



def show_ashnai(request):
    template = 'karbar/ashnai.html'
    return render(request, template, {'ashnai': karbar.darbare_ma.ashnai_text()
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : 'madadju'
                                      , 'username' : ''})


def show_sakhtar_sazmani(request):
    template = 'karbar/sakhtar_sazmani.html'
    return render(request, template, {'sakhtar_sazmani': karbar.darbare_ma.sakhtar_sazmani_text()
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : 'madadju'
                                      ,'username':''})

def show_moshahede_list_koodakan(request):
    template = 'karbar/moshahede_list_koodakan.html'
    madadjuyan = Madadju.objects.all()
    return render(request, template, {'madadjuyan':[(m.first_name,Niaz.objects.filter(niazmand=m),Niaz.niaz_taminnashode(m)) for m in madadjuyan]
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : 'madadju'
                                      ,'username':''})

def show_moshahede_list_niazhaye_fori_taminnashode(request):
    template = 'karbar/moshahede_list_niazhaye_fori_taminnashode.html'
    madadjuyan = Madadju.objects.all()
    return render(request, template, {'madadjuyan':[( m.first_name, ((niaz.onvan,niaz.mablagh_taminnashode()) for niaz in Niaz.niaz_taminnashode(m).filter(niazFori=True))) for m in madadjuyan]
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : 'madadju'
                                      ,'username':''})