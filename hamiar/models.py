from django.db import models
import datetime


# Create your models here.
from modir.models import *


class Hamiar(staff_members):
    mojudi = models.PositiveIntegerField(default=0)
    termination_date = models.DateField(null=True,
                                        blank=True)  # age delete kard acountesho kolan hazfesh nemikonim. inja minevisim
    start_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=False)  # modir activesh mikone


class hemaiatNiaz(models.Model):
    hamiar = models.ForeignKey('Hamiar', on_delete=models.PROTECT)
    mablagh = models.PositiveIntegerField()  # mabaghi ke hamiar hemaiat karde
    niaz = models.ForeignKey('Niaz', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)  # age false bashe yani az hemaiat enseraf dade

    class Meta:
        unique_together = (("hamiar", "niaz"),)


class PardakhtNiaz(
    models.Model):  # in baraie gozaresh pardakht be kar mire. ghabli maslan ye bar miad vali age 100 mah hemaiat she inja sad bar miad
    niaz = models.ForeignKey('hemaiatNiaz', on_delete=models.PROTECT)
    mablagh = models.PositiveIntegerField()
    zaman = models.DateTimeField(default=datetime.now, blank=True)


class hemaiat_kheirieh(models.Model):
    hamiar = models.ForeignKey('Hamiar', on_delete=models.PROTECT)
    mablagh = models.PositiveIntegerField()  # mabaghi ke hamiar hemaiat karde
    kheirieh = models.ForeignKey('kheirieh', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)  # age false bashe yani az hemaiat enseraf dade

    class Meta:
        unique_together = (("hamiar", "kheirieh"),)



