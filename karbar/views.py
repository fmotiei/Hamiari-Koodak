from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
import karbar.darbare_ma
from django.views.decorators.csrf import csrf_exempt
from .forms import SignUpForm, SignInForm
from .models import *
from karbar import moshtarak
import hamiar
from karbar.models import *
from madadju.models import Madadju, Niaz

def user_type(user):
    userkarbarInstance = karbar.models.UserKarbar.objects.get(user=user)
    if userkarbarInstance.is_hamiar:
        return 'hamiar'
    elif userkarbarInstance.is_madadkar:
        return 'madadkar'
    elif userkarbarInstance.is_madadju:
        return 'madadju'


def show_profile(request):
    template = 'karbar/index.html'
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


def show_sabtename_hamyar(request):
    template = 'karbar/sabtename_hamyar.html'
    if request.method == 'GET':
        form = SignUpForm()
        return  render(request, template, {'form': form, 'utype' : 'karbar'
        , 'progress': karbar.darbare_ma.progress()
        , 'username':''
        , 'roydadha' : {} })


    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            if User.objects.filter(username=username).exists():
                return render(request, template, {'form': form, 'utype' : 'karbar'
        , 'progress': karbar.darbare_ma.progress()
        , 'username':''
        , 'roydadha' : {} })

            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            ukarbar=UserKarbar.objects.create(user=user, phone_number=phone_number, address=address, is_hamiar=True)
            staff=staff_members.objects.create(stafID=ukarbar )
            hamiar.models.Hamiar.objects.create(staffID=staff )
            login(request, user)
            return render(request, 'karbar/regiset_success.html', {'form': form})
            # return HttpResponseRedirect(reverse("hamyar_panel")+"?success=1")  # this should be hamyar's own page
        else:
            return render(request, template, {'form': form})


def show_ahdaf(request):
    return moshtarak.show_ahdaf(request,'karbar')

def show_ashnai(request):
    return moshtarak.show_ashnai(request,'karbar')


def show_sakhtar_sazmani(request):
    return moshtarak.show_sakhtar_sazmani(request,'karbar')

def show_moshahede_list_koodakan(request):
    return moshtarak.show_moshahede_list_koodakan(request,'karbar')

def show_moshahede_list_niazhaye_fori_taminnashode(request):
    return moshtarak.show_moshahede_list_niazhaye_fori_taminnashode(request,'karbar')

def show_register_success(request):
    return render(request,"karbar/regiset_success.html")
