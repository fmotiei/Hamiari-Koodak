from django.db import models
from django import forms
from django.core.validators import RegexValidator


# Create your models here.
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



class staff_members(User):
    pardakhti = models.PositiveIntegerField()#jame harchi ke pardakht kardan (momkene maslan madadkar az jib bezare)
    dariafti = models.PositiveIntegerField() #jame har chi dariaft kardan


class ModirArshad(staff_members):
    hoghugh = models.PositiveIntegerField()


class ModirKarshenas(staff_members):
    hoghugh = models.PositiveIntegerField()

