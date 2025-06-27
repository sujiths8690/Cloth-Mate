from django.contrib import admin

from .models import BankAd,UserClass,AccountType
# Register your models here.
admin.site.register(BankAd)
admin.site.register(UserClass)
admin.site.register(AccountType)