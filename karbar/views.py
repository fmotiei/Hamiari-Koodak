from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse
import karbar.darbare_ma

# Create your views here.
from madadju.models import Madadju, Niaz


def show_moshahede_list_koodakan(request):
    template = 'karbar/moshahede_list_koodakan.html'
    madadjuyan = Madadju.objects.all()
    return render(request, template, {'madadjuyan':[(m.first_name,Niaz.objects.filter(niazmand=m),Niaz.niaz_taminnashode(m)) for m in madadjuyan]
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : 'karbar'})

def show_moshahede_list_niazhaye_fori_taminnashode(request):
    template = 'karbar/moshahede_list_niazhaye_fori_taminnashode.html'
    madadjuyan = Madadju.objects.all()
    return render(request, template, {'madadjuyan':[( m.first_name, ((niaz.onvan,niaz.mablagh_taminnashode()) for niaz in Niaz.niaz_taminnashode(m).filter(niazFori=True))) for m in madadjuyan]
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : 'karbar'})

def show_profile(request):
    template = 'karbar/index.html'
    return render(request, template, {'tozihat':karbar.darbare_ma.tozihat_text()
                                        ,'images':karbar.darbare_ma.akhbar_image()
                                        ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : 'karbar'})


def show_sabtename_hamyar(request):
    template = 'karbar/sabtename_hamyar.html'
    return render(request, template, {'progress':karbar.darbare_ma.progress()})
#TODO bayad vurudi bekhunim az html


def show_ahdaf(request):
    template = 'karbar/ahdaf.html'
    return render(request, template, {'ahdaf': karbar.darbare_ma.ahdaf_text()
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : 'karbar'})


def show_ashnai(request):
    template = 'karbar/ashnai.html'
    return render(request, template, {'ashnai': karbar.darbare_ma.ashnai_text()
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : 'karbar'})


def show_sakhtar_sazmani(request):
    template = 'karbar/sakhtar_sazmani.html'
    return render(request, template, {'sakhtar_sazmani': karbar.darbare_ma.sakhtar_sazmani_text()
                                      ,'progress':karbar.darbare_ma.progress()
                                      ,'utype' : 'karbar'})
