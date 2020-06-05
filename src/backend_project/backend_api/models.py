from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# ....................... #

from django.contrib.auth.models import BaseUserManager

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.apps import apps
from django.dispatch import receiver
from django.db.models.signals import pre_migrate
from django.db import connection
from django.core.management import call_command
from django.conf import settings
from django.db.utils import ProgrammingError

from . import conf


COUNTRY_CHOICES= [
    ('Europe/London', 'Europe/London'),
    ('Asia/Kolkata', 'Asia/Kolkata'),
    ('America/Los_Angeles', 'America/Los_Angeles'),
    ('Asia/Shanghai', 'Asia/Shanghai'),
    ]


if conf.AUTOCREATE_DB:
    @receiver(pre_migrate, sender=apps.get_app_config('activity_log'))
    def createdb(sender, using, **kwargs):
        db = settings.DATABASES[conf.LOG_DB_KEY]['NAME']
        with connection.cursor() as cursor:
            try:
                cursor.execute("CREATE DATABASE {}".format(db))
            except ProgrammingError:
                pass

        if using == 'default':
            call_command('migrate', database=conf.LOG_DB_KEY)


class ActivityLog(models.Model):
    user_id = models.CharField(_('user id'), max_length=10)
    user = models.CharField(_('user'), max_length=256)
    user_location = models.CharField(_('user location'), max_length=256, choices=COUNTRY_CHOICES)
    activity_period = models.ManyToManyField("ActivityPeriod", blank=True)

    class Meta:
        verbose_name = _('activity log')

class ActivityPeriod(models.Model):
    start_time = models.DateTimeField(_('start_time'), default=timezone.now)
    end_time = models.DateTimeField(_('end_time'), default=timezone.now)

    def get_full_period(self):
        self.start_time = timezone.now()
        self.end_time = timezone.now()
        self.save(update_fields=["start_time", "end_time"])
        value = "start_time = " + str(self.start_time) + "\n" + "end_time = " + str(self.end_time)

        return value

class UserMixin(models.Model):
    last_activity = models.DateTimeField(
        _('last activity'), default=timezone.now, editable=False)

    def update_last_activity(self):
        self.last_activity = timezone.now()
        self.save(update_fields=["last_activity"])

    class Meta:
        abstract = True


class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, email, name, password=None):
        """Creates a new user profile."""

        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given details."""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Represents a "user profile" inside out system. Stores all user account
    related data, such as 'email address' and 'name'.
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Django uses this when it needs to get the user's full name."""

        return self.name

    def get_short_name(self):
        """Django uses this when it needs to get the users abbreviated name."""

        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to text."""

        return self.email
