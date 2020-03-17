from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Member(models.Model):
    """ User model """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    CIVILITY_PARAMS = [
        ('Mrs', _('Madame')),
        ('Ms', _('Miss')),
        ('Mr', _('Mister')),
    ]
    tel = models.CharField(_('Phone number'), blank=True, max_length=20)
    civility = models.CharField(max_length=10,
                                choices=CIVILITY_PARAMS,
                                blank=True)
    birthday = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
