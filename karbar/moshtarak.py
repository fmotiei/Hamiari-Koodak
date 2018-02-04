from django.shortcuts import render
from karbar.forms import  SignInForm
import karbar
from karbar.models import Payam, Payam_Madadju, Payam_Adi
from madadju.models import Madadju, Niaz
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

def user_type(user):
    userkarbarInstance = karbar.models.UserKarbar.objects.get(user=user)
    if userkarbarInstance.is_hamiar:
        return 'hamiar'
    elif userkarbarInstance.is_madadkar:
        return 'madadkar'
    elif userkarbarInstance.is_madadju:
        return 'madadju'


def show_user(request,user):
    template = 'karbar/index.html'
    return render(request, template, {'tozihat': karbar.darbare_ma.tozihat_text()
        , 'images': karbar.darbare_ma.akhbar_image()
        , 'progress': karbar.darbare_ma.progress()
        , 'utype': user
        , 'username': request.user })
#TODO login


def show_afzayesh_etebar(request,user):
    template = 'karbar/afzayesh_etebar.html'
    return render(request, template, {'utype' : user
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : request.user})
#TODO etebar ra begirad va afzayesh dahad


def show_ersal_payam(request,user):
    template = 'karbar/ersal_payam.html'
    return render(request, template, {'utype' : user
                                    , 'progress': karbar.darbare_ma.progress()
                                    ,'username' : request.user})
#TODO shenase o onvan o matn ro begire va payam ro befreste

def show_moshahede_tarakonesh_haye_mali(request,user):
    template = 'karbar/moshahede_tarakonesh_haye_mali.html'
    return render(request, template, {'utype' : user
                                        , 'progress': karbar.darbare_ma.progress()
                                        , 'tarakoneshha' : []
                                        , 'username': request.user})
#TODO bayd tarakonesh haye mali ro behesh befrestim onvan,mablagh,user,day,hour

def show_payam_daryafti(request,user):
    template = 'karbar/payam_daryafti.html'
    return render(request, template, {'utype' : user
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username':request.user
                                    , 'onvan': ''
                                    , 'text' : ''
                                    , 'sender': ''
                                    , 'date': ''})
#TODO onvan matne payam tarkh va fersatnde



def show_payam_ersali(request,user):
    template = 'karbar/payam_ersali.html'
    return render(request, template, {'utype': user
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username': request.user
                                    , 'onvan': ''
                                    , 'text': ''
                                    , 'receiver': ''
                                    , 'date': ''})
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
    payamha = []
    if user == 'madadju':
        for payam in Payam_Madadju.objects.all() :
            if payam.sender.user.user == request.user :
                payamha.append((payam.id,payam.reciever.staffID.stafID.user.username,payam.zaman,payam.onvan))
    for payam in Payam_Adi.objects.all() :
        if payam.sender.user.user == request.user :
            payamha.append((payam.id,payam.reciever,payam.zaman,payam.onvan))
    return render(request, template, {'utype': user
        , 'progress': karbar.darbare_ma.progress()
        , 'username': request.user
        , 'payamha': payamha })
    # TODO payamha shamele upayam,receiver,zaman,onvan


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
    if request.method == 'GET':
        form = SignInForm()

        return render(request, template, {'form': form, 'utype' : user
        , 'progress': karbar.darbare_ma.progress()
        , 'username':''
        , 'ahdaf': karbar.darbare_ma.ahdaf_text()})

    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.confirm_login_allowed(request):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is None:
                message = 'گذرواژه اشتباه ‌است'
                args = {'form': form, 'message': message ,'utype' : user
        , 'progress': karbar.darbare_ma.progress()
        , 'ahdaf': karbar.darbare_ma.ahdaf_text() }
                return render(request, template, args)
            else:
                utype=user_type(user)
                login(request, user)
                return HttpResponseRedirect('/'+utype+'/'+"?success=1")
        else:
            message = 'نام کاربری شما در سامانه ثبت نشده است'
            args = {'form': form, 'message': message, 'utype' : user
        , 'progress': karbar.darbare_ma.progress()
        , 'username':''
        , 'ahdaf': karbar.darbare_ma.ahdaf_text() }
            return render(request, template, args)

def show_ashnai(request,user):
    template = 'karbar/ashnai.html'
    return render(request, template, {'ashnai': karbar.darbare_ma.ashnai_text()
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : user
                                      , 'username' : request.user})
    # return render(request, template, {'ashnai': karbar.darbare_ma.ashnai_text()
    #                                   ,'progress':karbar.darbare_ma.progress()
    #                                   ,'utype' : user
    #                                   , 'username' : ''})

    if request.method == 'GET':
        form = SignInForm()

        return render(request, template, {'form': form, 'utype' : user
        , 'progress': karbar.darbare_ma.progress()
        ,'ashnai': karbar.darbare_ma.ashnai_text()})

    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.confirm_login_allowed(request):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is None:
                message = 'گذرواژه اشتباه ‌است'
                args = {'form': form, 'message': message ,'utype' : user
        , 'progress': karbar.darbare_ma.progress(),
                        'ashnai': karbar.darbare_ma.ashnai_text() }
                return render(request, template, args)
            else:
                utype=user_type(user)
                login(request, user)
                return HttpResponseRedirect('/'+utype+'/'+"?success=1")
        else:
            message = 'نام کاربری شما در سامانه ثبت نشده است'
            args = {'form': form, 'message': message, 'utype' : user
        , 'progress': karbar.darbare_ma.progress()
        , 'username':''
        ,'ashnai': karbar.darbare_ma.ashnai_text() }
            return render(request, template, args)

def show_sakhtar_sazmani(request,user):
    template = 'karbar/sakhtar_sazmani.html'
    # return render(request, template, {'sakhtar_sazmani': karbar.darbare_ma.sakhtar_sazmani_text()
    #                                   ,'progress':karbar.darbare_ma.progress()
    #                                   ,'utype' : user
    #                                   ,'username':''})
    if request.method == 'GET':
        form = SignInForm()

        return render(request, template, {'form': form, 'utype' : user
        , 'progress': karbar.darbare_ma.progress()
        ,'sakhtar_sazmani': karbar.darbare_ma.sakhtar_sazmani_text()})

    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.confirm_login_allowed(request):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is None:
                message = 'گذرواژه اشتباه ‌است'
                args = {'form': form, 'message': message ,'utype' : user
        , 'progress': karbar.darbare_ma.progress(),
                        'sakhtar_sazmani': karbar.darbare_ma.sakhtar_sazmani_text() }
                return render(request, template, args)
            else:
                utype=user_type(user)
                login(request, user)
                return HttpResponseRedirect('/'+utype+'/'+"?success=1")
        else:
            message = 'نام کاربری شما در سامانه ثبت نشده است'
            args = {'form': form, 'message': message, 'utype' : user
        , 'progress': karbar.darbare_ma.progress()
        , 'username':''
        ,'sakhtar_sazmani': karbar.darbare_ma.sakhtar_sazmani_text() }
            return render(request, template, args)


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



def mylogin(template, request):
    if request.method == 'GET':
        form = SignInForm()

        return render(request, template, {'form': form, 'utype' : 'karbar'
        , 'progress': karbar.darbare_ma.progress()
        , 'username':''
        , 'roydadha' : {} })

    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.confirm_login_allowed(request):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is None:
                message = 'گذرواژه اشتباه ‌است'
                args = {'form': form, 'message': message ,'utype' : 'karbar'
        , 'progress': karbar.darbare_ma.progress()
        , 'roydadha' : {} }
                return render(request, template, args)
            else:
                utype=user_type(user)
                login(request, user)
                return HttpResponseRedirect('/'+utype+'/'+"?success=1")
        else:
            message = 'نام کاربری شما در سامانه ثبت نشده است'
            args = {'form': form, 'message': message, 'utype' : 'karbar'
        , 'progress': karbar.darbare_ma.progress()
        , 'username':''
        , 'roydadha' : {} }
            return render(request, template, args)
