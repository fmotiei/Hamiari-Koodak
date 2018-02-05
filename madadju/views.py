from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse


# Create your views here.
import karbar
from hamiar.models import hemaiatNiaz, Hamiar, User
from karbar import moshtarak
from madadju.models import Madadju, Niaz, staff_members, UserKarbar,taghire_madadkar
from madadju.forms import taghirMadadkarForm

def is_madadju(user):
    if not UserKarbar.objects.filter(user=user).exists():
        return False
    else:
        userKarbar = UserKarbar.objects.get(user=user)
        return Madadju.objects.filter(user = userKarbar).exists()


@login_required(login_url='/karbar/')
@user_passes_test(is_madadju,login_url='/karbar/')
def show_darkhast_taghir_madadkar(request):
    template = 'madadju/darkhast.html'
    userKarbar = UserKarbar.objects.get(user=request.user)
    madadju = Madadju.objects.get(user=userKarbar)
    if request.method == "GET":
        form=taghirMadadkarForm()
        return render(request, template, {'utype' : 'madadju'
                                    , 'progress': karbar.darbare_ma.progress()
                                    ,'username' : request.user
                                      , 'mName' : madadju.madadkar.staffID.stafID.user.username,'form':form})
    if request.method == "POST":
        form=taghirMadadkarForm(request.POST)
        if form.is_valid():
            sharh = form.cleaned_data['sharh']
            taghire_madadkar.objects.create(madadju=madadju,sharh=sharh)
            return moshtarak.show_amaliat_movafagh(request, 'madadju')
        else:
            return render(request, template, {'utype': 'madadju'
                , 'progress': karbar.darbare_ma.progress()
                , 'username': request.user
                , 'mName': madadju.madadkar.staffID.stafID.user.username, 'form': form})


@login_required(login_url='/karbar/')
@user_passes_test(is_madadju,login_url='/karbar/')
def show_profile(request):
    template = 'madadju/profile.html'
    userKarbar = UserKarbar.objects.get(user=request.user)
    madadju = Madadju.objects.get(user=userKarbar)
    niazha = []
    for niaz in hemaiatNiaz.objects.all() :
        if niaz.niaz.niazmand == madadju :
            niazha.append(niaz)
    hamiarha = []
    for niaz in niazha :
        if not hamiarha.__contains__(niaz.hamiar.username()):
            hamiarha.append(niaz.hamiar.username())
    return render(request, template, {'utype' : 'madadju'
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : request.user
                                    , 'first_name': request.user.first_name
                                    , 'last_name': request.user.last_name
                                    , 'alarm': madadju.ekhtar
                                    , 'madadkar': madadju.madadkar.staffID.stafID.user.username
                                    , 'hamiarha': hamiarha })

@login_required(login_url='/karbar/')
@user_passes_test(is_madadju,login_url='/karbar/')
def show_niaz_haye_madadju(request):
    template = 'madadju/niaz_haye_madadju.html'
    madadju_un = request.user
    user = User.objects.get(username=madadju_un)
    userKarbar = UserKarbar.objects.get(user=user)
    madadju = Madadju.objects.get(user=userKarbar)
    niazha = []
    for niaz in Niaz.objects.all():
        if niaz.niazmand == madadju:
            niazha.append(niaz)
    return render(request, template, {'username' : request.user,
                                      'progress': karbar.darbare_ma.progress(),
                                      'niazha' :[( n.id, n.onvan, n.mablagh-n.mablagh_taminshodeh, n.mablagh_taminshodeh, n.niazFori) for n in niazha], # [ (type(n.niazmand),1,1,1) for n in Niaz.objects.all()],#= 'Madadju object (1)')],
                                      'madadju_un' : madadju_un,
                                      'madadju_alarm' : madadju.ekhtar
                                      })


@login_required(login_url='/karbar/')
@user_passes_test(is_madadju,login_url='/karbar/')
def show_hamiar_profile(request):
    template = 'madadju/hamiar_profile.html'
    hamiarName = request.GET.get('hamiar')
    user = User.objects.get(username=hamiarName)
    userKarbar = UserKarbar.objects.get(user=user)
    staffMember = staff_members.objects.get(stafID=userKarbar)
    hamiar = Hamiar.objects.get(staffID = staffMember)
    niazha = []
    for niaz in hemaiatNiaz.objects.all() :
        if niaz.hamiar == hamiar :
            niazha.append(niaz)
    madadjuyan = []
    for niaz in niazha :
        if not madadjuyan.__contains__(niaz.niaz.niazmand):
            madadjuyan.append(niaz.niaz.niazmand.user.user.username)
    return render(request, template, {'utype' : 'madadju'
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : request.user
                                      , 'husername' : user.username
                                      , 'hfName' : user.first_name
                                      , 'hlName' : user.last_name
                                      , 'madadjuyan' : madadjuyan})

@login_required(login_url='/karbar/')
@user_passes_test(is_madadju,login_url='/karbar/')
def show_madadju(request):
    return moshtarak.show_user(request,'madadju')

@login_required(login_url='/karbar/')
@user_passes_test(is_madadju,login_url='/karbar/')
def show_afzayesh_etebar(request):
    return moshtarak.show_afzayesh_etebar(request,'madadju')

@login_required(login_url='/karbar/')
@user_passes_test(is_madadju,login_url='/karbar/')
def show_ersal_payam(request):
    return moshtarak.show_ersal_payam(request,'madadju')

@login_required(login_url='/karbar/')
@user_passes_test(is_madadju,login_url='/karbar/')
def show_moshahede_tarakonesh_haye_mali(request):
    return moshtarak.show_moshahede_tarakonesh_haye_mali(request,'madadju')

@login_required(login_url='/karbar/')
@user_passes_test(is_madadju,login_url='/karbar/')
def show_payam_daryafti(request):
    return moshtarak.show_payam_daryafti(request,'madadju')

@login_required(login_url='/karbar/')
@user_passes_test(is_madadju,login_url='/karbar/')
def show_payam_ersali(request):
    return moshtarak.show_payam_ersali(request,'madadju')

@login_required(login_url='/karbar/')
@user_passes_test(is_madadju,login_url='/karbar/')
def show_roydadha(request):
    return moshtarak.show_roydadha(request,'madadju')

@login_required(login_url='/karbar/')
@user_passes_test(is_madadju,login_url='/karbar/')
def show_sandoghe_payamhaye_daryafti(request):
    return moshtarak.show_sandoghe_payamhaye_daryafti(request,'madadju')

@login_required(login_url='/karbar/')
@user_passes_test(is_madadju,login_url='/karbar/')
def show_sandoghe_payamhaye_ersali(request):
    return moshtarak.show_sandoghe_payamhaye_ersali(request,'madadju')

@login_required(login_url='/karbar/')
@user_passes_test(is_madadju,login_url='/karbar/')
def show_amaliat_movafagh(request):
    return moshtarak.show_amaliat_movafagh(request,'madadju')

@login_required(login_url='/karbar/')
@user_passes_test(is_madadju,login_url='/karbar/')
def show_ahdaf(request):
    return moshtarak.show_ahdaf(request,'madadju')

@login_required(login_url='/karbar/')
@user_passes_test(is_madadju,login_url='/karbar/')
def show_ashnai(request):
    return moshtarak.show_ashnai(request,'madadju')

@login_required(login_url='/karbar/')
@user_passes_test(is_madadju,login_url='/karbar/')
def show_sakhtar_sazmani(request):
    return moshtarak.show_sakhtar_sazmani(request,'madadju')

@login_required(login_url='/karbar/')
@user_passes_test(is_madadju,login_url='/karbar/')
def show_moshahede_list_koodakan(request):
    return moshtarak.show_moshahede_list_koodakan(request,'madadju')

@login_required(login_url='/karbar/')
@user_passes_test(is_madadju,login_url='/karbar/')
def show_moshahede_list_niazhaye_fori_taminnashode(request):
    return moshtarak.show_moshahede_list_niazhaye_fori_taminnashode(request,'madadju')
