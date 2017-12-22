from django.db import models
import datetime

# Create your models here.
class Payam(models.Model):
    onvan = models.CharField(max_length=30)
    matn = models.CharField(max_length=1000)
    zaman = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        abstract = True


class Payam_Adi(Payam):
    sender = models.ForeignKey('staff_members', null=False)
    reciever = models.ForeignKey('User')


class Payam_Madadju(Payam):
    sender = models.ForeignKey('Madadju', null=False)
    reciever = models.ForeignKey('Hamiar')
    taieed = models.BooleanField(default=False)


class Payam_Madadju_Madadkar(Payam):
    sender = models.ForeignKey('Madadju', null=False)
    reciever = models.ForeignKey('Madadkar')
    Type = (
        ('GD', 'تشکر'),
        ('NU', 'پیشنهاد'),
        ('BD', 'انتقاد')
    )


class events(models.Model):
    onvan = models.CharField(max_length=30)
    matn = models.CharField(max_length=100)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
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
