from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse


# Create your views here.
import karbar
from karbar import moshtarak
from madadju.models import Madadju, Niaz


def show_afzoudan_niaz(request):
    template = 'madadkar/afzoudan_niaz.html'
    return render(request, template, {'progress': karbar.darbare_ma.progress()})
#todo transform form fields to db

def show_moshahede_madadjuyan_taht_kefalat(request):
    template = 'madadkar/moshahede_madadjuyan_taht_kefalat.html'
    return render(request, template, {'username' : '',
                                      'progress': karbar.darbare_ma.progress(),
                                      'madadjuyan': [(m.username, m.first_name, m.last_name, m.ekhtar) for m in []]
        #Madadju.objects.filter(madadkar!=Null)
                                      #todo link moshahede profile madadju
                                      })


def show_niaz_haye_madadju(request):
    template = 'madadkar/niaz_haye_madadju.html'
    return render(request, template, {'username' : '',
                                      'progress': karbar.darbare_ma.progress(),
                                      'niazha' : [( n.onvan, n.mablagh-n.mablagh_taminshodeh, n.mablagh_taminshodeh, n.niazFori) for n in []],
                                      #todo all niazha for this madadju
                                      'madadju_un' : '',
                                      'madadju_mablagh' : '',
                                      'madadju_taminshode' :'',
                                      'madadju_alarm' : ''
                                      #todo madadju(un, mablagh, taminshode) fill for 1 madadju
                                      })

def show_niaz_haye_tamin_nashode(request):
    template = 'madadkar/niaz_haye_tamin_nashode.html'
    return render(request, template, {'username' : '',
                                      'progress': karbar.darbare_ma.progress(),
                                      'niazha': [(n.niazmand.username, n.onvan, n.mablagh,n.niazFori) for n in []],
                                      # todo niazhaye tamin nashode baraye hame madadju
                                      'madadjuyan' : [m.username for m in []],
                                      #todo hame madadjuha
                                      })


def show_niaz_haye_tamin_nashode_fori(request):
    template = 'madadkar/niaz_haye_tamin_nashode_fori.html'
    return render(request, template, {'username' : '',
                                      'progress': karbar.darbare_ma.progress(),
                                      'niazha': [(n.niazmand.username, n.onvan, n.mablagh, n.niazFori) for n in []],
                                      # todo niazhaye tamin nashode fori baraye hame madadju
                                      'madadjuyan': [m.username for m in []],
                                      # todo hame madadjuha

                                      })

def show_payam_entezar(request):
    template = 'madadkar/payam_entezar.html'
    return render(request, template, {'username' : '',
                                      'progress': karbar.darbare_ma.progress(),
                                      'msg' : '',
                                      'header' : '',
                                      'rcvr' : '',
                                      #todo reciver ro bayad kole obj ro dashtebashim
                                      'time' : ''
                                      })


def show_profile(request):
    template = 'madadkar/profile.html'
    return render(request, template, {'username' : '',
                                      'progress': karbar.darbare_ma.progress(),

                                      })


def show_profile_madadju(request):
    template = 'madadkar/profile_madadju.html'
    return render(request, template, {'username' : '',
                                      'progress': karbar.darbare_ma.progress()})

def show_sandoghe_payamhaye_entezar(request):
    template = 'madadkar/sandoghe_payamhaye_entezar.html'
    return render(request, template, {'username' : '',
                                      'progress': karbar.darbare_ma.progress()})


def show_sabte_naam_madadju(request):
    template = 'madadkar/sabte_naam_madadju.html'
    return render(request, template, {'username' : '',
                                      'progress': karbar.darbare_ma.progress()})


def show_virayesh_niaz(request):
    template = 'madadkar/virayesh_niaz.html'
    return render(request, template, {'username' : '',
                                      'progress': karbar.darbare_ma.progress()})


def show_vaziat_tahsili(request):
    template = 'madadkar/vaziat_tahsili.html'
    return render(request, template, {'username' : '',
                                      'progress': karbar.darbare_ma.progress()})


def show_moshahede_madadjuyan_dar_entezar_madadkar(request):
    template = 'madadkar/moshahede_madadjuyan_dar_entezar_madadkar.html'
    return render(request, template, {'progress': karbar.darbare_ma.progress(),
                                      'madadjuyan': [(m.first_name, m.last_name) for m in []],
                                  #    Madadju.objects.filter(madadkar='Null')
                                      'username' : ''
                                      #todo link moshahede profile madadju
                                      })


def show_profile_madadju_bi_kefalat(request):
    template = 'madadkar/profile_madadju_bi_kefalat.html'
    return render(request, template, {'username' : '',
                                      'progress': karbar.darbare_ma.progress()})

def show_niaz_haye_madadju_bi_kefalat(request):
    template = 'madadkar/niaz_haye_madadju_bi_kefalat.html'
    return render(request, template, {'username' : '',
                                      'progress': karbar.darbare_ma.progress(),
                                      'niazha': [(n.onvan, n.mablagh - n.mablagh_taminshodeh, n.mablagh_taminshodeh,
                                                  n.niazFori) for n in []],
                                      # todo all niazha for this madadju
                                      'madadju_un': '',
                                      'madadju_mablagh': '',
                                      'madadju_taminshode': '',
                                      'madadju_alarm': ''
                                      # todo madadju(un, mablagh, taminshode) fill for 1 madadju
                                      })



def show_madadkar(request):
    return moshtarak.show_user(request,'madadkar')


def show_afzayesh_etebar(request):
    return moshtarak.show_afzayesh_etebar(request,'madadkar')


def show_ersal_payam(request):
    return moshtarak.show_ersal_payam(request,'madadkar')

def show_moshahede_tarakonesh_haye_mali(request):
    return moshtarak.show_moshahede_tarakonesh_haye_mali(request,'madadkar')

def show_payam_daryafti(request):
    return moshtarak.show_payam_daryafti(request,'madadkar')

def show_payam_ersali(request):
    return moshtarak.show_payam_ersali(request,'madadkar')


def show_roydadha(request):
    return moshtarak.show_roydadha(request,'madadkar')


def show_sandoghe_payamhaye_daryafti(request):
    return moshtarak.show_sandoghe_payamhaye_daryafti(request,'madadkar')


def show_sandoghe_payamhaye_ersali(request):
    return moshtarak.show_sandoghe_payamhaye_ersali(request,'madadkar')


def show_amaliat_movafagh(request):
    return moshtarak.show_amaliat_movafagh(request,'madadkar')

def show_ahdaf(request):
    return moshtarak.show_ahdaf(request,'madadkar')

def show_ashnai(request):
    return moshtarak.show_ashnai(request,'madadkar')


def show_sakhtar_sazmani(request):
    return moshtarak.show_sakhtar_sazmani(request,'madadkar')

def show_moshahede_list_koodakan(request):
    return moshtarak.show_moshahede_list_koodakan(request,'madadkar')

def show_moshahede_list_niazhaye_fori_taminnashode(request):
    return moshtarak.show_moshahede_list_niazhaye_fori_taminnashode(request,'madadkar')