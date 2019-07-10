from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
import datetime

class Part(models.Model):
    part = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.part

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    full_name = models.CharField(_('氏名'), max_length=150, null=True)
    #first_name = models.CharField(_('first name'), max_length=30, blank=True)
    #last_name = models.CharField(_('last name'), max_length=150, blank=True)
    part = models.ForeignKey(Part, verbose_name=_('所属') ,on_delete=models.PROTECT, null=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),    
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active.'
            'Unselect this instead if deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name= _('user')
        verbose_name_plural = _('users')
    
    def get_full_name(self):
        #full_name = '%s %s' %(self.first_name, self.last_name)
        return self.full_name

    def get_short_name(self):
        return self.full_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def username(self):
        return self.full_name

    

# Create your models here.
class Place(models.Model):
    pl = models.CharField(max_length=100)

    def __str__(self):
        return self.pl

class Atted_Person(models.Model):
    AP = models.CharField(max_length=100)



class Practice(models.Model):
    date = models.DateTimeField()
    manu = models.TextField(blank=True)
    Place_Category = models.ForeignKey(Place, on_delete=models.PROTECT)

    def __str__(self):
        return self.date.strftime("%m/%d")

class Check_attend(models.Model):
    check_attend = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.check_attend

class Attend(models.Model):
    practice = models.ForeignKey(Practice, on_delete=models.PROTECT)
    member = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    check_attend = models.ForeignKey(Check_attend, on_delete=models.PROTECT, null=True)
    comment = models.TextField(blank=True)

    class Meta:
        unique_together =('practice', 'member')

