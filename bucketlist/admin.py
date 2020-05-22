from django.contrib import admin
from .models import Bucketlist, Bucketlistitem, Account
# Register your models here.

admin.site.register(Account)
admin.site.register(Bucketlist)
admin.site.register(Bucketlistitem)
