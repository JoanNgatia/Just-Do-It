from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Account(AbstractBaseUser):
    """Extend Django's built -in User model that inherits from AbstractUser."""

    username = models.CharField(max_length=80, unique=True)
    email = models.EmailField(unique=True)

    tagline = models.CharField(max_length=140)

    is_admin = models.BooleanField(default=False)

    # specify the required field and default username field
    USERNAME_FIELD = 'username'

    def __unicode__(self):
        """Display string representation of username."""
        return self.username


class Base(models.Model):
    """Create common base class for bucketlist and item creation."""

    name = models.CharField(max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['updated_at']


class Bucketlist(Base):
    """Extend and customize base model."""

    creator = models.ForeignKey(Account)

    class Meta(Base.Meta):
        """Extend parent meta class."""

        db_table = 'bucketlist'

    def __unicode__(self):
        """Display string representation of bucketlistname."""
        return self.name


class Bucketlistitem(Base):
    """Extend and customize base bucektlistitem model."""

    done = models.BooleanField(default=False)
    bucketlist = models.ForeignKey(Bucketlist)

    class Meta(Base.Meta):
        """Extend parent meta class."""

        db_table = 'Bucketlistitem'

    def __unicode__(self):
        """Display string representation of bucketlistitemname."""
        return self.name
