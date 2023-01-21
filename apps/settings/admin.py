from django.contrib import admin
from apps.settings.models import Setting, Contact

# Register your models here.
admin.site.register(Setting)
admin.site.register(Contact)