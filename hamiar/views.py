from django.contrib.auth.models import User
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse


# Create your views here.
import karbar
from hamiar.models import hemaiatNiaz, Hamiar
from karbar import moshtarak
from karbar.models import UserKarbar, staff_members
from madadju.models import Madadju, Niaz

def show_hemayat_az_moasese(request):
    template = 'hamiar/hemayat_az_moasese.html'
    return render(request, template, {'utype':'hamiar'
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : request.user })
#TODO mablagh ro begire va b hesab moassese (?) ezafe kone
#todo YEGANE

def show_hemayat_az_niaz(request):
    template = 'hamiar/hemayat_az_niaz.html'
    return render(request, template, {'utype':'hamiar'
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : request.user
                                    , 'niazName' : ''
                                      , 'hazineTaminShode' : ''
                                      , 'hazineTaminNashode' : ''
                                      , 'fori' : '' })
#TODO username: username karbar , niazName : name niaz , hazine ha va fori marbut b niaz

def show_moshahede_niaz_haye_taht_hemayat(request):
    template = 'hamiar/moshahede_niaz_haye_taht_hemayat.html'
    user = User.objects.get(username=request.user)
    userKarbar = UserKarbar.objects.get(user=user)
    staffMember = staff_members.objects.get(stafID=userKarbar)
    hamiar = Hamiar.objects.get(staffID=staffMember)
    niazha = []
    for niaz in hemaiatNiaz.objects.all():
        if niaz.hamiar == hamiar:
            niazha.append(niaz)
    madadjuyan = []
    for niaz in niazha:
        if not madadjuyan.__contains__(niaz.niaz.niazmand):
            madadjuyan.append(niaz.niaz.niazmand)
    madadjus = []
    for madadju in madadjuyan :
        niazs = []
        for niaz in niazha :
            if niaz.niaz.niazmand == madadju :
                niazs.append((niaz.niaz.id,niaz.niaz.onvan,niaz.niaz.mablagh_taminshodeh,niaz.niaz.mablagh_taminnashode(),niaz.niaz.niazFori))
        madadjus.append((madadju.user.user.username,niazs))

    return render(request, template, {'utype':'hamiar'
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : request.user
                                      , 'madadjuyan' : madadjus })
#TODO ba zadane enseraf enseraf dahad

def show_niaz_haye_tamin_nashode(request):
    template = 'hamiar/niaz_haye_tamin_nashode.html'
    niazha = []
    for niaz in Niaz.objects.all():
        if niaz.hemaiatshod == False:
            niazha.append(niaz)
    return render(request, template, {'utype':'hamiar'
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : request.user
                                      , 'niazha': [(n.niazmand.username, n.onvan, n.mablagh,n.niazFori) for n in niazha]
                                      })
#TODO ba zadane hemayat hemayat konad

def show_niaz_haye_madadju(request):
    template = 'hamiar/niaz_haye_madadju.html'
    madadju_un = request.GET.get('madadju_un')
    user = User.objects.get(username=madadju_un)
    userKarbar = UserKarbar.objects.get(user=user)
    madadju = Madadju.objects.get(user=userKarbar)
    niazha = []
    for niaz in Niaz.objects.all():
        if niaz.niazmand == madadju:
            niazha.append(niaz)
    return render(request, template, {'utype':'hamiar'
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : request.user,
                                      'niazha': [(n.id, n.onvan, n.mablagh - n.mablagh_taminshodeh,
                                                  n.mablagh_taminshodeh, n.niazFori) for n in niazha],
                                      'madadju_un': madadju_un, })

def show_profile(request):
    template = 'hamiar/profile.html'
    userKarbar = UserKarbar.objects.get(user=request.user)
    staffMember = staff_members.objects.get(stafID=userKarbar)
    hamiar = Hamiar.objects.get(staffID=staffMember)
    madadjuha = []
    for niaz in hemaiatNiaz.objects.filter(hamiar=hamiar):
            madadjuha.append(niaz.niazmand.username())
    return render(request, template, {'utype':'hamiar'
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : request.user
                                      , 'fn' : request.user.first_name
                                      , 'ln' : request.user.last_name
                                      , 'madadjuyan' : madadjuha
                                      , 'etebar' : userKarbar.mojudi
                                    })

def show_profile_madadju(request):
    template = 'hamiar/profile_madadju.html'
    madadju_un = request.GET.get('madadju_un')
    user = User.objects.get(username=madadju_un)
    userKarbar = UserKarbar.objects.get(user=user)
    madadju = Madadju.objects.get(user=userKarbar)
    return render(request, template, {'utype':'hamiar',
                                      'username': request.user,
                                     'progress': karbar.darbare_ma.progress(),
                                      'alarm': madadju.ekhtar,
                                      'progress': karbar.darbare_ma.progress(),
                                      'madadju_un': request.GET.get('madadju_un'),
                                      'src': request.GET.get('src'),
                                      'madadju_fn': user.first_name,
                                      'madadju_ln': user.last_name,
                                      'madadkar_un':madadju.madadkar,
                                      'sharh': "onvan" + "-" + "sharh"})
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