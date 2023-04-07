from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.settings.models import Setting, PhoneNumber ,Partners, Contact, Gallery, FAQ, News, Promotion, Benefit, Team,WeAre, About

# Register your models here.
class SettingAdmin(TranslationAdmin):
    list_display = ('title', 'description')

class BenefitAdmin(TranslationAdmin):
    list_display = ('title', 'description')

admin.site.register(Setting, SettingAdmin)
admin.site.register(PhoneNumber)
admin.site.register(Contact)
admin.site.register(Gallery)
admin.site.register(FAQ)
admin.site.register(News)
admin.site.register(Promotion)
admin.site.register(Benefit, BenefitAdmin)
admin.site.register(Team)
admin.site.register(WeAre)
admin.site.register(Partners)
admin.site.register(About)