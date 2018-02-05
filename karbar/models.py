from django.db import models
from .models import *
from django.contrib.auth.models import User

from datetime import datetime


class UserKarbar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    address = models.CharField(max_length=100)
    mojudi = models.PositiveIntegerField(default=0 )
    phone_number = models.CharField( max_length=17, blank=True)  # validators should be a list
    is_hamiar = models.BooleanField( default=False)
    is_madadkar = models.BooleanField( default=False)
    is_madadju = models.BooleanField( default=False)
    def __str__(self):
        return self.user.username
    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)



class staff_members(models.Model):
    stafID =  models.OneToOneField(
        UserKarbar,
        on_delete=models.CASCADE,
        primary_key=True, default=''
    )
    def __str__(self):
        return self.stafID.user.username


# Create your models here.
class Payam(models.Model):
    onvan = models.CharField(max_length=30)
    matn = models.CharField(max_length=1000)
    zaman = models.DateTimeField(default=datetime.now, blank=True)


class Payam_Adi(models.Model):
    payam = models.OneToOneField(Payam,on_delete=models.CASCADE,primary_key=True,default='')
    sender = models.ForeignKey(staff_members, null=False, on_delete=models.PROTECT,related_name='Sender')
    reciever = models.ForeignKey(User, on_delete=models.PROTECT,related_name='Reciever')


class Payam_Madadju(models.Model):
    payam = models.OneToOneField(Payam,on_delete=models.CASCADE,primary_key=True,default='')
    sender = models.ForeignKey('madadju.Madadju', null=False,  on_delete=models.PROTECT)
    reciever = models.ForeignKey('hamiar.Hamiar', on_delete=models.PROTECT)
    taieed = models.BooleanField(default=False)


class Payam_Madadju_Madadkar(models.Model):
    payam = models.OneToOneField(Payam,on_delete=models.CASCADE,primary_key=True,default='')
    sender = models.ForeignKey('madadju.Madadju', null=False, on_delete=models.PROTECT)
    reciever = models.ForeignKey('madadkar.Madadkar', on_delete=models.PROTECT)
    Type = (
        ('GD', 'تشکر'),
        ('NU', 'پیشنهاد'),
        ('BD', 'انتقاد')
    )


class events(models.Model):
    onvan = models.CharField(max_length=30)
    matn = models.CharField(max_length=100)
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    zaman = models.DateTimeField(default=datetime.now, blank=True)


class kheirieh(models.Model):  # omur kheirieh tahte hemaiat sazman
    onvan = models.CharField(max_length=30, primary_key=True)
    matn = models.CharField(max_length=100)
    mablagh = models.PositiveIntegerField()
    mablagh_taminshode = models.PositiveIntegerField(default=0)


class akhbar(models.Model):
    onvan = models.CharField(max_length=30)
    matn = models.CharField(max_length=100)
    zaman = models.DateTimeField(default=datetime.now, blank=True)

class Payment(models.Model):
    mablagh = models.PositiveIntegerField(default=0)
    onvan = models.CharField(default='', max_length=50)
    pardakht_konande = models.ForeignKey(UserKarbar, null=False, on_delete=models.PROTECT,related_name='pardakht_konande')
    girande = models.ForeignKey(UserKarbar, null=False, on_delete=models.PROTECT,related_name='girande')
    zaman = models.DateTimeField(default=datetime.now, blank=True)
