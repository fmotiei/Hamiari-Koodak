from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse


# Create your views here.
import karbar
from karbar import moshtarak
from madadju.models import Madadju, Niaz

def show_hemayat_az_moasese(request):
    template = 'hamiar/hemayat_az_moasese.html'
    return render(request, template, {'utype':'hamiar'
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : ''})
#TODO html b DB username: username karbar

def show_hemayat_az_niaz(request):
    template = 'hamiar/hemayat_az_niaz.html'
    return render(request, template, {'utype':'hamiar'
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : ''
                                    , 'niazName' : ''
                                      , 'hazineTaminShode' : ''
                                      , 'hazineTaminNashode' : ''
                                      , 'fori' : '' })
#TODO username: username karbar , niazName : name niaz , hazine ha va fori marbut b niaz

def show_moshahede_niaz_haye_taht_hemayat(request):
    template = 'hamiar/moshahede_niaz_haye_taht_hemayat.html'
    return render(request, template, {'utype':'hamiar'
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : ''
                                      , 'madadjuyan' : [] })
#TODO username: username karbar, madadjuyan : name,niazha k niazha : onvan , hazine tamin shode va nashode , fori marbut b niaz

def show_niaz_haye_tamin_nashode(request):
    template = 'hamiar/niaz_haye_tamin_nashode.html'
    return render(request, template, {'utype':'hamiar'
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : ''
                                      , 'madadjuyan' : [] })
#TODO username: username karbar, madadjuyan : name,niazha k niazha : onvan , hazine tamin shode va nashode , fori marbut b niaz

def show_niaz_haye_tamin_nashode_fori(request):
    template = 'hamiar/niaz_haye_tamin_nashode_fori.html'
    return render(request, template, {'utype':'hamiar'
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : ''
                                      , 'madadjuyan' : [] })
#TODO username: username karbar, madadjuyan : name,niazha k niazha : onvan , hazine tamin shode va nashode , fori marbut b niaz

def show_niaz_haye_madadju(request):
    template = 'hamiar/niaz_haye_madadju.html'
    return render(request, template, {'utype':'hamiar'
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : ''
                                      , 'alarm' : ''
                                      , 'name' : ''
                                      , 'niazha' : [] })
#TODO username: username karbar, niazha : onvan , hazine tamin shode va nashode , fori marbut b niaz

def show_profile(request):
    template = 'hamiar/profile.html'
    return render(request, template, {'utype':'hamiar'
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : ''
                                      , 'fn' : ''
                                      , 'ln' : ''
                                      , 'madadjuyan' : []
                                      , 'etebar' : ''})
#TODO username : username karbar , fn : first name karbar , ln : last name karbar , madadjuyan : username madadjuyan marbut b karbar , etebar : etebare karbar

def show_profile_madadju(request):
    template = 'hamiar/profile_madadju.html'
    return render(request, template, {'utype':'hamiar'
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : ''
                                      ,'mName' : ''
                                      , 'alarm' : ''
                                      , 'mfName' : ''
                                      , 'mlName' : ''
                                      , 'hamiaran': []
                                      , 'vaziatUmumi' : ''})
#TODO username : username karbar , mName: esme madadju , alarm : alarme madadju , mlName: familie madadju , hamiaran araye az esme hamiaran marbut b madadju , vaziatUmumi : vaziat tahsili umumi madadju
#TODO bayad madadju ra baraye list niaz hayash befrestad


def show_hamiar(request):
    return moshtarak.show_user(request,'hamiar')


def show_afzayesh_etebar(request):
    return moshtarak.show_afzayesh_etebar(request,'hamiar')


def show_ersal_payam(request):
    return moshtarak.show_ersal_payam(request,'hamiar')

def show_moshahede_tarakonesh_haye_mali(request):
    return moshtarak.show_moshahede_tarakonesh_haye_mali(request,'hamiar')

def show_payam_daryafti(request):
    return moshtarak.show_payam_daryafti(request,'hamiar')

def show_payam_ersali(request):
    return moshtarak.show_payam_ersali(request,'hamiar')


def show_roydadha(request):
    return moshtarak.show_roydadha(request,'hamiar')


def show_sandoghe_payamhaye_daryafti(request):
    return moshtarak.show_sandoghe_payamhaye_daryafti(request,'hamiar')


def show_sandoghe_payamhaye_ersali(request):
    return moshtarak.show_sandoghe_payamhaye_ersali(request,'hamiar')


def show_amaliat_movafagh(request):
    return moshtarak.show_amaliat_movafagh(request,'hamiar')

def show_ahdaf(request):
    return moshtarak.show_ahdaf(request,'hamiar')

def show_ashnai(request):
    return moshtarak.show_ashnai(request,'hamiar')


def show_sakhtar_sazmani(request):
    return moshtarak.show_sakhtar_sazmani(request,'hamiar')

def show_moshahede_list_koodakan(request):
    return moshtarak.show_moshahede_list_koodakan(request,'hamiar')

def show_moshahede_list_niazhaye_fori_taminnashode(request):
    return moshtarak.show_moshahede_list_niazhaye_fori_taminnashode(request,'hamiar')