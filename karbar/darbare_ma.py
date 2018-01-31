import glob

from django.shortcuts import render

import karbar
from madadju.models import Niaz


def ashnai_text():
    return 'این یک موسسه خیریه است'

def ahdaf_text():
    return 'هدف کمک به کودکان با استعداد است.'

def sakhtar_sazmani_text():
    return '/static/img/sakhtar.jpg' # badan url image bedim

def tozihat_text():
    return 'بنیاد خیریه کودک تلاش میکند تا هیچ کودک مستعدی بی سرپرست و دور از تحصیل نماند.'

def akhbar_image():
    images = []
    images.append('kid2.jpg')
    images.append('kid3.jpg')
    return images

def progress():
    pr = []
    niaz = 100
    if( Niaz.objects.count() != 0 ):
        niaz = 100 * Niaz.objects.filter(mablagh_taminshodeh=0).count()/Niaz.objects.count()
    pr.append([niaz,'٪ نیازهای مددجویان تامین شده است.'])
    return pr