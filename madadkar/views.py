from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
import karbar
import madadju
from hamiar.models import hemaiatNiaz
from karbar import moshtarak
from madadju.models import Madadju, Niaz, Madadkar, UserKarbar, staff_members


def show_afzoudan_niaz(request):
    template = 'madadkar/afzoudan_niaz.html'
    return render(request, template, {'progress': karbar.darbare_ma.progress(),
                                      'username': request.user})
#todo transform form fields to db

def show_moshahede_madadjuyan_taht_kefalat(request):
    template = 'madadkar/moshahede_madadjuyan_taht_kefalat.html'
    user = request.user
    userKarbar = UserKarbar.objects.get(user=request.user)
    staffMember = staff_members.objects.get(stafID=userKarbar)
    madadkar = Madadkar.objects.get(staffID=staffMember)

    return render(request, template, {'username' : request.user,
                                      'progress': karbar.darbare_ma.progress(),
                                      'madadjuyan': [(m.user.user.username , m.user.user.first_name, m.user.user.last_name, m.ekhtar) for m in Madadju.objects.filter(madadkar=madadkar)]#filter(user_user_id = user.id)]
        #Madadju.objects.filter(madadkar!=Null)
                                      #todo link moshahede profile madadju
                                      })

@login_required
def show_niaz_haye_madadju(request):
    template = 'madadkar/niaz_haye_madadju.html'
    madadju_un = request.GET.get('madadju_un')
    user = User.objects.get(username=madadju_un)
    userKarbar = UserKarbar.objects.get(user=user)
    madadju = Madadju.objects.get(user=userKarbar)
    niazha = []
    for niaz in Niaz.objects.all():
        if niaz.niazmand == madadju:
            niazha.append(niaz)
    return render(request, template, {'username' : request.user,
                                      'progress': karbar.darbare_ma.progress(),
                                      'niazha' :[( n.onvan, n.mablagh-n.mablagh_taminshodeh, n.mablagh_taminshodeh, n.niazFori) for n in niazha], # [ (type(n.niazmand),1,1,1) for n in Niaz.objects.all()],#= 'Madadju object (1)')],
                                      'madadju_un' : madadju_un,
                                      'madadju_alarm' : madadju.ekhtar
                                      })

def show_niaz_haye_tamin_nashode(request):
    template = 'madadkar/niaz_haye_tamin_nashode.html'
    niazha = []
    for niaz in Niaz.objects.all():
        if niaz.hemaiatshod == False:
            niazha.append(niaz)
    return render(request, template, {'username' : request.user,
                                      'progress': karbar.darbare_ma.progress(),
                                      'niazha': [(n.niazmand.username, n.onvan, n.mablagh,n.niazFori) for n in niazha],
                                      })


def show_niaz_haye_tamin_nashode_fori(request):
    template = 'madadkar/niaz_haye_tamin_nashode_fori.html'
    niazha = []
    for niaz in Niaz.objects.all():
        if niaz.hemaiatshod == False:
            if niaz.niazFori:
                niazha.append(niaz)
    return render(request, template, {'username': request.user,
                                      'progress': karbar.darbare_ma.progress(),
                                      'niazha': [(n.niazmand.username, n.onvan, n.mablagh, n.niazFori) for n in niazha],
                                      })

#todo FAEZE
def show_payam_entezar(request):
    template = 'madadkar/payam_entezar.html'
    return render(request, template, {'username' : request.user,
                                      'progress': karbar.darbare_ma.progress(),
                                      'msg' : '',
                                      'header' : '',
                                      'rcvr' : '',
                                      #todo reciver ro bayad kole obj ro dashtebashim
                                      'time' : ''
                                      })


def show_profile(request):
    template = 'madadkar/profile.html'
    userKarbar = UserKarbar.objects.get(user=request.user)
    staffMember = staff_members.objects.get(stafID=userKarbar)
    # madadkar = Madadkar.objects.get(staffID=staffMember)
    return render(request, template, {'username' : request.user,
                                      'progress': karbar.darbare_ma.progress(),
                                      'first_name': request.user.first_name,
                                      'last_name': request.user.last_name,
                                      'etebar': staffMember.dariafti - staffMember.pardakhti
                                      })


def show_profile_madadju(request):
    template = 'madadkar/profile_madadju.html'
    madadju_un = request.GET.get('madadju_un')
    user = User.objects.get(username = madadju_un)
    userKarbar = UserKarbar.objects.get(user=user)
    madadju = Madadju.objects.get(user=userKarbar)
    niazha = []
    for niaz in hemaiatNiaz.objects.all():
        if niaz.niaz.niazmand == madadju:
            niazha.append(niaz)
    hamiarha = []
    for niaz in niazha:
        if not hamiarha.__contains__(niaz.hamiar):
            hamiarha.append(niaz.hamiar.staffID.stafID.user.username)

    return render(request, template, {'username' : madadju_un,
                                      'alarm':madadju.ekhtar,
                                      'progress': karbar.darbare_ma.progress(),
                                      'madadju_un' : request.GET.get('madadju_un'),
                                      'src':request.GET.get('src'),
                                      'madadju_fn' : user.first_name,
                                      'madadju_ln' : user.last_name,
                                      'hamiars': hamiarha,
                                      'sharh': "onvan" + "-" + "sharh"
                                      # 'sharh_kh': (madadju.sharhe_tahsil.Field_Taghir, madadju.sharhe_tahsil.ُType)
                                      })

#todo FAEZEH
def show_sandoghe_payamhaye_entezar(request):
    template = 'madadkar/sandoghe_payamhaye_entezar.html'
    return render(request, template, {'username' : request.user,
                                      'progress': karbar.darbare_ma.progress()})

#todo YEGANE
def show_sabte_naam_madadju(request):
    template = 'madadkar/sabte_naam_madadju.html'
    return render(request, template, {'username' : request.user,
                                      'progress': karbar.darbare_ma.progress()})

#todo YEGANE
def show_virayesh_niaz(request):
    template = 'madadkar/virayesh_niaz.html'
    return render(request, template, {'username' : request.user,
                                      'progress': karbar.darbare_ma.progress()})


def show_vaziat_tahsili(request):
    template = 'madadkar/vaziat_tahsili.html'
    return render(request, template, {'username' : request.user,
                                      'un': request.GET.get('madadju_un'),
                                      'progress': karbar.darbare_ma.progress()})


def show_moshahede_madadjuyan_dar_entezar_madadkar(request):
    template = 'madadkar/moshahede_madadjuyan_dar_entezar_madadkar.html'
    return render(request, template, {'progress': karbar.darbare_ma.progress(),
                                      'madadjuyan': [(m.username,m.user.user.first_name, m.user.user.last_name) for m in Madadju.objects.filter(madadkar=None)],
                                  #    Madadju.objects.filter(madadkar='Null')
                                      'username' : request.user
                                      #todo link moshahede profile madadju
                                      })


def show_profile_madadju_bi_kefalat(request):
    template = 'madadkar/profile_madadju_bi_kefalat.html'
    madadju_un = request.GET.get('madadju_un')
    user = User.objects.get(username=madadju_un)
    userKarbar = UserKarbar.objects.get(user=user)
    madadju = Madadju.objects.get(user=userKarbar)
    niazha = []
    for niaz in hemaiatNiaz.objects.all():
        if niaz.niaz.niazmand == madadju:
            niazha.append(niaz)
    hamiarha = []
    for niaz in niazha:
        if not hamiarha.contains(niaz.hamiar):
            hamiarha.append(niaz.hamiar.staffID.stafID.user.username)

    return render(request, template, {'username' : request.user,
                                      'alarm':madadju.ekhtar,
                                      'progress': karbar.darbare_ma.progress(),
                                      'madadju_un' : request.GET.get('madadju_un'),
                                      'madadju_fn' : user.first_name,
                                      'madadju_ln' : user.last_name,
                                      'hamiars': hamiarha,
                                      'sharh': "onvan" + "-" + "sharh"
                                      })

def show_niaz_haye_madadju_bi_kefalat(request):
    template = 'madadkar/niaz_haye_madadju_bi_kefalat.html'
    madadju_un = request.GET.get('madadju_un')
    user = User.objects.get(username=madadju_un)
    userKarbar = UserKarbar.objects.get(user=user)
    madadju = Madadju.objects.get(user=userKarbar)
    niazha = []
    for niaz in Niaz.objects.all():
        if niaz.niazmand == madadju:
            niazha.append(niaz)
    return render(request, template, {'username' : request.user,
                                      'progress': karbar.darbare_ma.progress(),
                                      'niazha': [(n.onvan, n.mablagh - n.mablagh_taminshodeh, n.mablagh_taminshodeh,
                                                  n.niazFori) for n in niazha],
                                      'madadju_un': madadju_un,
                                      'madadju_alarm': madadju.ekhtar
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