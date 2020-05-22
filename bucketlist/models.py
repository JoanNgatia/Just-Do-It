from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    """Extend django's user model with added fields."""

    tagline = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Base(models.Model):
    """Create common base class for bucketlist and item creation."""

    name = models.CharField(max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Extend parent meta class."""

        abstract = True
        ordering = ['-updated_at']


class Bucketlist(Base):
    """Extend and customize base model."""

    creator = models.ForeignKey(Account, related_name='bucketlists')

    class Meta(Base.Meta):
        """Extend parent meta class."""

        db_table = 'bucketlist'

    def __unicode__(self):
        """Display string representation of bucketlistname."""
        return self.name


class Bucketlistitem(Base):
    """Extend and customize base model for bucketlistitems."""

    done = models.BooleanField(default=False)
    bucketlist = models.ForeignKey(Bucketlist, related_name='items')

    class Meta(Base.Meta):
        """Extend parent meta class."""

        db_table = 'Bucketlistitem'

    def __unicode__(self):
        """Display string representation of bucketlistitemname."""
        return self.name
