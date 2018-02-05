import glob

from django.shortcuts import render

import karbar
from madadju.models import Niaz


def ashnai_text():
    f = open('static/text/ashnai.txt')
    return f.read()

def ahdaf_text():
    f = open('static/text/ahdaf.txt')
    return f.read()

def sakhtar_sazmani_text():
    return '/static/img/sakhtar.jpg' # badan url image bedim

def tozihat_text():
    f = open('static/text/tozihat.txt')
    return f.read()

def akhbar_image():
    images = []
    images.append('kid2.jpg')
    images.append('kid3.jpg')
    return images

def progress():
    pr = []
    niaz = 100
    if( len(Niaz.objects.all()) != 0 ):
        niaz = 100 * len(Niaz.objects.filter(mablagh_taminshodeh=0))/len(Niaz.objects.all())
    pr.append([niaz,'٪ نیازهای مددجویان تامین شده است.'])
    return pr