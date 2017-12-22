from django.db import models
from madadju.models import *
from madadkar.models import *
from modir.models import *
from hamiar.models import *

from datetime import datetime
class User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    online = models.BooleanField()  # is online
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


# class Meta:
#    abstract = True


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = '__all__'



class staff_members(User):
    pardakhti = models.PositiveIntegerField()#jame harchi ke pardakht kardan (momkene maslan madadkar az jib bezare)
    dariafti = models.PositiveIntegerField() #jame har chi dariaft kardan

# Create your models here.
class Payam(models.Model):
    onvan = models.CharField(max_length=30)
    matn = models.CharField(max_length=1000)
    zaman = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        abstract = True


class Payam_Adi(Payam):
    sender = models.ForeignKey(staff_members, null=False, on_delete=models.PROTECT,related_name='Sender')
    reciever = models.ForeignKey(User, on_delete=models.PROTECT,related_name='Reciever')


class Payam_Madadju(Payam):
    sender = models.ForeignKey('madadju.Madadju', null=False,  on_delete=models.PROTECT)
    reciever = models.ForeignKey('hamiar.Hamiar', on_delete=models.PROTECT)
    taieed = models.BooleanField(default=False)


class Payam_Madadju_Madadkar(Payam):
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
