import glob

from django.shortcuts import render

import karbar
from karbar.models import akhbar
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
    if not len(Niaz.objects.all()) == 0 :
        sumMablagh = 0
        sumTamin = 0
        for niaz in Niaz.objects.all():
            sumMablagh = sumMablagh + niaz.mablagh
            sumTamin = sumTamin + niaz.mablagh_taminshodeh
        niaz = int(100 * sumTamin / sumMablagh)
    pr.append([niaz,'٪ تامین نیازها'])
    return pr