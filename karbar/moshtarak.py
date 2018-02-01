from django.shortcuts import render

import karbar
from madadju.models import Madadju


def show_user(request,user):
    template = 'karbar/index.html'
    return render(request, template, {'tozihat': karbar.darbare_ma.tozihat_text()
        , 'images': karbar.darbare_ma.akhbar_image()
        , 'progress': karbar.darbare_ma.progress()
        , 'utype': user
        , 'username': ''})


def show_afzayesh_etebar(request,user):
    template = 'karbar/afzayesh_etebar.html'
    return render(request, template, {'utype' : user
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : ''})
#TODO html to DB


def show_ersal_payam(request,user):
    template = 'karbar/ersal_payam.html'
    return render(request, template, {'utype' : user
                                    , 'progress': karbar.darbare_ma.progress()
                                    ,'username' : ''})

def show_moshahede_tarakonesh_haye_mali(request,user):
    template = 'karbar/moshahede_tarakonesh_haye_mali.html'
    return render(request, template, {'utype' : user
                                        , 'progress': karbar.darbare_ma.progress()
                                        , 'tarakoneshha' : {}
                                        , 'username': ''})
#TODO bayd tarakonesh haye mali ro behesh befrestim

def show_payam_daryafti(request,user):
    template = 'karbar/payam_daryafti.html'
    return render(request, template, {'utype' : user
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username':''
                                    , 'onvan': ''
                                    , 'text' : ''
                                    , 'sender': ''
                                    , 'day': ''
                                    , 'hour' : ''})
#TODO onvan matne payam tarkh va fersatnde



def show_payam_ersali(request,user):
    template = 'karbar/payam_ersali.html'
    return render(request, template, {'utype': user
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username': ''
                                    , 'onvan': ''
                                    , 'text': ''
                                    , 'sender': ''
                                    , 'day': ''
                                    , 'hour': ''})
#TODO onvan matne payam tarkh va fersatnde


def show_roydadha(request,user):
    template = 'karbar/roydadha.html'
    return render(request, template, {'utype' : user
        , 'progress': karbar.darbare_ma.progress()
        , 'username':''
        , 'roydadha' : {} })
#TODO roydadha shamel onvan,text,day,hour


def show_sandoghe_payamhaye_daryafti(request,user):
    template = 'karbar/sandoghe_payamhaye_daryafti.html'
    return render(request, template, {'utype': user
        , 'progress': karbar.darbare_ma.progress()
        , 'username': ''
        , 'payamha': {}})
#TODO payamha shamele sender,day,hour,onvan


def show_sandoghe_payamhaye_ersali(request,user):
    template = 'karbar/sandoghe_payamhaye_ersali.html'
    return render(request, template, {'utype': user
        , 'progress': karbar.darbare_ma.progress()
        , 'username': ''
        , 'payamha': {}})
    # TODO payamha shamele receiver,day,hour,onvan


def show_amaliat_movafagh(request,user):
    template = 'karbar/amaliat_movafagh.html'
    return render(request, template, {'utype' : user
                                      , 'progress': karbar.darbare_ma.progress()
                                      ,'username':''})

def show_hamiar_pri(request,user):
    template = 'karbar/ahdaf.html'
    return render(request, template, {'ahdaf': karbar.darbare_ma.ahdaf_text()
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : user
                                      ,'username':''})


def show_ahdaf(request,user):
    template = 'karbar/ahdaf.html'
    return render(request, template, {'ahdaf': karbar.darbare_ma.ahdaf_text()
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : user
                                      ,'username':''})

def show_ashnai(request,user):
    template = 'karbar/ashnai.html'
    return render(request, template, {'ashnai': karbar.darbare_ma.ashnai_text()
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : user
                                      , 'username' : ''})


def show_sakhtar_sazmani(request,user):
    template = 'karbar/sakhtar_sazmani.html'
    return render(request, template, {'sakhtar_sazmani': karbar.darbare_ma.sakhtar_sazmani_text()
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : user
                                      ,'username':''})

def show_moshahede_list_koodakan(request,user):
    template = 'karbar/moshahede_list_koodakan.html'
    madadjuyan = Madadju.objects.all()
    return render(request, template, {'madadjuyan':[(m.first_name,Niaz.objects.filter(niazmand=m),Niaz.niaz_taminnashode(m)) for m in madadjuyan]
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : user
                                      ,'username':''})

def show_moshahede_list_niazhaye_fori_taminnashode(request,user):
    template = 'karbar/moshahede_list_niazhaye_fori_taminnashode.html'
    madadjuyan = Madadju.objects.all()
    return render(request, template, {'madadjuyan':[( m.first_name, ((niaz.onvan,niaz.mablagh_taminnashode()) for niaz in Niaz.niaz_taminnashode(m).filter(niazFori=True))) for m in madadjuyan]
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : user
                                      ,'username':''})
