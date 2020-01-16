from django.contrib import admin

# Register your models here.

from .models import CodesUser, Meeting

admin.site.register(CodesUser)

admin.site.register(Meeting)