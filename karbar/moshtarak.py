from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
import datetime
from hamiar.models import PardakhtNiaz, Hamiar
from karbar.forms import  SignInForm, ErsalPayamForm
import karbar
from karbar.models import Payam, Payam_Madadju, Payam_Adi, UserKarbar, staff_members, events,Payam_Madadju_Madadkar
from madadju.models import Madadju, Niaz
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from karbar.models import Payment
from hamiar.forms import afzayeshEtebar
from madadkar.models import Madadkar, hoghugh_dariafti


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

@login_required
def show_afzayesh_etebar(request,user):
    template = 'karbar/afzayesh_etebar.html'
    if request.method == 'GET':
        form = afzayeshEtebar()
        return render(request, template, {'form':form,'utype' : user
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : request.user})
    if request.method == 'POST':
        form = afzayeshEtebar(request.POST)
        if form.is_valid():
            afzayesh=form.cleaned_data['mablagh']
            userUK = User.objects.get(username=request.user)
            ukarbar=UserKarbar.objects.get(user=userUK)
            ukarbar.mojudi += afzayesh
            ukarbar.save()
            Payment.objects.create(onvan='افزایش اعتبار',mablagh=afzayesh,pardakht_konande=ukarbar,girande=ukarbar,zaman=datetime.datetime.now())
            template = 'karbar/amaliat_movafagh.html'
            return render(request, template, {'utype': user
                , 'progress': karbar.darbare_ma.progress()
                , 'username': ''})
        else:
            return render(request, template, {'form':form,'utype' : user
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username' : request.user})
#TODO etebar ra begirad va afzayesh dahad (bara hamiar mikone)

@login_required
def show_ersal_payam(request,user):
    template = 'karbar/ersal_payam.html'
    if request.method == 'GET':
        form = ErsalPayamForm()
        return render(request, template, {'form':form, 'utype' : user
                                    , 'progress': karbar.darbare_ma.progress()
                                    ,'username' : request.user})
    if request.method == 'POST':
        form = ErsalPayamForm(request.POST)
        if form.is_valid():
            recieverUN=form.cleaned_data['reciever']
            onvan=form.cleaned_data['onvan']
            matn=form.cleaned_data['matn']
            if User.objects.filter(username=recieverUN).exists():
                recieverUser=User.objects.get(username=recieverUN)
            else:
                return render(request, template, {'form': form, 'utype': user
                    , 'progress': karbar.darbare_ma.progress()
                    , 'username': request.user, 'message':'نام کاربری گیرنده در سیستم موجود نیست.'})

            userUK = User.objects.get(username=request.user)
            ukarbar=UserKarbar.objects.get(user=userUK)
            if staff_members.objects.filter(stafID=ukarbar).exists():# halati ke ye staff payam mide
                ustmember = staff_members.objects.get(stafID=ukarbar)
                Payam_Adi.objects.create(sender=ustmember, reciever=recieverUser,onvan=onvan,matn=matn, zaman=datetime.datetime.now())
                template = 'karbar/amaliat_movafagh.html'
                return render(request, template, {'utype': user
                    , 'progress': karbar.darbare_ma.progress()
                    , 'username': ''})

            else: #halati ke madadju payam mide :D
                ustmember = Madadju.objects.get(user=ukarbar)
                recieverUkarbar = UserKarbar.objects.get(user= recieverUser)
                if staff_members.objects.filter(stafID=recieverUkarbar).exists():
                    recieverStaff=staff_members.objects.get(stafID=recieverUkarbar)
                    if Hamiar.objects.filter(staffID=recieverStaff).exists(): #payam madadju be hamiar
                        recieverhamiar=Hamiar.objects.get(staffID=recieverStaff)
                        Payam_Madadju.objects.create(sender=ustmember, reciever=recieverhamiar,onvan=onvan,matn=matn, zaman=datetime.datetime.now(),taieed=False)
                        template = 'karbar/amaliat_movafagh.html'
                        return render(request, template, {'utype': user
                            , 'progress': karbar.darbare_ma.progress()
                            , 'username': ''})
                    else: #payam madadju be madadkar
                        if Madadkar.objects.filter(staffID=recieverStaff):
                            recieverMadadkar = Madadkar.objects.get(staffID=recieverStaff)
                            Payam_Madadju_Madadkar.objects.create(sender=ustmember, reciever=recieverMadadkar,onvan=onvan,matn=matn, zaman=datetime.datetime.now(),taieed=False)
                            template = 'karbar/amaliat_movafagh.html'
                            return render(request, template, {'utype': user
                                , 'progress': karbar.darbare_ma.progress()
                                , 'username': ''})
                        else:
                            return render(request, template, {'form': form, 'utype': user
                                , 'progress': karbar.darbare_ma.progress()
                                , 'username': request.user,
                                                              'message': 'نام کاربری فرستنده باید نام کاربری یک همیار یا مددکار باشد.'})
                else:
                    return render(request, template, {'form': form, 'utype': user
                        , 'progress': karbar.darbare_ma.progress()
                        , 'username': request.user, 'message': 'نام کاربری فرستنده باید نام کاربری یک همیار یا مددکار باشد.'})
        else:
            return render(request, template, {'form': form, 'utype': user
                , 'progress': karbar.darbare_ma.progress()
                , 'username': request.user})


@login_required
def show_moshahede_tarakonesh_haye_mali(request,user):
    template = 'karbar/moshahede_tarakonesh_haye_mali.html'
    tarakoneshha = []
    if user == 'hamiar':
        userKarbar = UserKarbar.objects.get(user = request.user)
        staffMember = staff_members.objects.get(stafID = userKarbar)
        hamiar = Hamiar.objects.get(staffID=staffMember)
        for tarakonesh in PardakhtNiaz.objects.all() :
            if tarakonesh.niaz.hamiar == hamiar :
                tarakoneshha.append(('پرداخت نیاز',tarakonesh.mablagh,request.user.username,tarakonesh.zaman))

    if user == 'madadju':
        userKarbar = UserKarbar.objects.get(user = request.user)
        madadju = Madadju.objects.get(user=userKarbar)
        for tarakonesh in PardakhtNiaz.objects.all() :
            if tarakonesh.niaz.niaz.niazmand == madadju :
                tarakoneshha.append(('تامین نیاز',tarakonesh.mablagh,tarakonesh.niaz.hamiar.username(),tarakonesh.zaman))

    if user == 'madadkar' :
        userKarbar = UserKarbar.objects.get(user=request.user)
        staffMember = staff_members.objects.get(stafID=userKarbar)
        madadkar = Madadkar.objects.get(staffID=staffMember)
        for tarakonesh in hoghugh_dariafti.objects.all():
            if tarakonesh.maddadkar == madadkar :
                tarakoneshha.append(('پرداخت حقوق',tarakonesh.mablagh,'موسسه',tarakonesh.zaman))


    return render(request, template, {'utype' : user
                                        , 'progress': karbar.darbare_ma.progress()
                                        , 'tarakoneshha' : tarakoneshha
                                        , 'username': request.user})
#TODO (onvan,mablagh,user,date)    bazi tarakonesh ha ro nadarim k :(


@login_required
def show_payam_daryafti(request, user):
    template = 'karbar/payam_daryafti.html'
    upayam = request.GET.get('payam')
    try:
        payam = Payam_Madadju.objects.get(id=upayam)
    except ObjectDoesNotExist:
        try:
            payam = Payam_Adi.objects.get(id=upayam)
        except :
            payam = Payam_Madadju_Madadkar.objects.get(id=upayam)

    return render(request, template, {'utype': user
        , 'progress': karbar.darbare_ma.progress()
        , 'username': request.user
        , 'onvan': payam.onvan
        , 'text': payam.matn
        , 'sender': payam.sender.username()
        , 'date': payam.zaman})


@login_required
def show_payam_ersali(request,user):
    template = 'karbar/payam_ersali.html'
    upayam = request.GET.get('payam')
    try:
        payam = Payam_Madadju.objects.get(id=upayam)
    except ObjectDoesNotExist:
        try:
            payam = Payam_Adi.objects.get(id=upayam)
        except :
            payam = Payam_Madadju_Madadkar.objects.get(id=upayam)

    return render(request, template, {'utype': user
                                    , 'progress': karbar.darbare_ma.progress()
                                    , 'username': request.user
                                    , 'onvan': payam.onvan
                                    , 'text': payam.matn
                                    , 'receiver': payam.reciever.username()
                                    , 'date': payam.zaman})

@login_required
def show_roydadha(request,user):
    template = 'karbar/roydadha.html'
    roydadha = events.objects.filter(user=request.user)
    roydadha = [(roydad.onvan,roydad.matn,roydad.zaman) for roydad in roydadha]
    return render(request, template, {'utype' : user
        , 'progress': karbar.darbare_ma.progress()
        , 'username': request.user
        , 'roydadha' : roydadha })
#TODO mishe ba zarbdar pak she ?

@login_required
def show_sandoghe_payamhaye_daryafti(request,user):
    template = 'karbar/sandoghe_payamhaye_daryafti.html'
    payamha = []
    if user == 'hamiar':
        for payam in Payam_Madadju.objects.all():
            if payam.reciever.staffID.stafID.user == request.user:
                payamha.append((payam.pk, payam.sender.username, payam.zaman, payam.onvan))

    if user == 'madadkar':
        for payam in Payam_Madadju_Madadkar.objects.all():
            if payam.reciever.staffID.stafID.user == request.user:
                payamha.append((payam.pk, payam.sender.username, payam.zaman, payam.onvan))
    for payam in Payam_Adi.objects.all():
        if payam.reciever == request.user:
            payamha.append((payam.pk, payam.sender.username , payam.zaman, payam.onvan))
    return render(request, template, {'utype': user
        , 'progress': karbar.darbare_ma.progress()
        , 'username': request.user
        , 'payamha': payamha})

@login_required
def show_sandoghe_payamhaye_ersali(request,user):
    template = 'karbar/sandoghe_payamhaye_ersali.html'
    payamha = []
    if user == 'madadju':
        for payam in Payam_Madadju.objects.all() :
            if payam.sender.user.user == request.user :
                payamha.append((payam.pk,payam.reciever.username,payam.zaman,payam.onvan))
    for payam in Payam_Adi.objects.all() :
        if payam.sender.user.user == request.user :
            payamha.append((payam.pk,payam.reciever.username,payam.zaman,payam.onvan))
    return render(request, template, {'utype': user
        , 'progress': karbar.darbare_ma.progress()
        , 'username': request.user
        , 'payamha': payamha })

@login_required
def show_amaliat_movafagh(request,user):
    template = 'karbar/amaliat_movafagh.html'
    return render(request, template, {'utype' : user
                                      , 'progress': karbar.darbare_ma.progress()
                                      ,'username':''})



def show_ahdaf(request,user):
    template = 'karbar/ahdaf.html'
    if request.method == 'GET':
        form = SignInForm()
        userName = ''
        if not user == 'karbar':
            userName = request.user
        return render(request, template, {'form': form, 'utype' : user
        , 'progress': karbar.darbare_ma.progress()
        , 'username': userName
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
    if request.method == 'GET':
        form = SignInForm()
        userName = ''
        if not user == 'karbar':
            userName = request.user
        return render(request, template, {'form': form, 'utype' : user
        , 'progress': karbar.darbare_ma.progress()
        ,'ashnai': karbar.darbare_ma.ashnai_text()
        , 'username': userName})

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
        userName = ''
        if not user == 'karbar':
            userName = request.user

        return render(request, template, {'form': form, 'utype' : user
        , 'progress': karbar.darbare_ma.progress()
        ,'sakhtar_sazmani': karbar.darbare_ma.sakhtar_sazmani_text()
        , 'username' : userName})

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
    if request.method == 'GET':
        form = SignInForm()
        userName = ''
        if not user == 'karbar':
            userName = request.user

        return render(request, template, {'form': form, 'madadjuyan':[(m.user.user.first_name,Niaz.objects.filter(niazmand=m),Niaz.niaz_taminnashode(m)) for m in madadjuyan]
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : user
                                      ,'username':userName})

    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.confirm_login_allowed(request):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is None:
                message = 'گذرواژه اشتباه ‌است'
                args = {'form': form, 'message': message, 'madadjuyan':[(m.user.user.first_name,Niaz.objects.filter(niazmand=m),Niaz.niaz_taminnashode(m)) for m in madadjuyan]
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : user
                                      ,'username':request.user}
                return render(request, template, args)
            else:
                utype = user_type(user)
                login(request, user)
                return HttpResponseRedirect('/' + utype + '/' + "?success=1")
        else:
            message = 'نام کاربری شما در سامانه ثبت نشده است'
            args = {'form': form, 'message': message, 'madadjuyan':[(m.user.user.first_name,Niaz.objects.filter(niazmand=m),Niaz.niaz_taminnashode(m)) for m in madadjuyan]
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : user
                                      ,'username':request.user}
            return render(request, template, args)

def show_moshahede_list_niazhaye_fori_taminnashode(request,user):
    template = 'karbar/moshahede_list_niazhaye_fori_taminnashode.html'
    madadjuyan = Madadju.objects.all()
    if request.method == 'GET':
        form = SignInForm()
        userName = ''
        if not user == 'karbar':
            userName = request.user

        return render(request, template, {'form': form, 'madadjuyan':[( m.user.user.first_name, ((niaz.onvan,niaz.mablagh_taminnashode()) for niaz in Niaz.objects.filter(niazFori=True))) for m in madadjuyan]
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : user
                                      ,'username':userName})

    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.confirm_login_allowed(request):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is None:
                message = 'گذرواژه اشتباه ‌است'
                args = {'form': form, 'message': message, 'madadjuyan':[( m.user.user.first_name, ((niaz.onvan,niaz.mablagh_taminnashode()) for niaz in Niaz.objects.filter(niazFori=True))) for m in madadjuyan]
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : user
                                      ,'username':request.user}
                return render(request, template, args)
            else:
                utype = user_type(user)
                login(request, user)
                return HttpResponseRedirect('/' + utype + '/' + "?success=1")
        else:
            message = 'نام کاربری شما در سامانه ثبت نشده است'
            args = {'form': form, 'message': message, 'madadjuyan':[( m.user.user.first_name, ((niaz.onvan,niaz.mablagh_taminnashode()) for niaz in Niaz.objects.filter(niazFori=True))) for m in madadjuyan]
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : user
                                      ,'username':request.user}
            return render(request, template, args)



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
