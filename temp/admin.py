from django.contrib import admin
from .models import Books, AboutPage, QrCode
                  
# Register your models here.
a = [Books, AboutPage, QrCode]
for i in a:
    admin.site.register(i)