from django.contrib import admin

from apps.settings.models import Setting,Partners, Contact, Gallery, FAQ, News, Promotion, Benefit, Team,WeAre

# Register your models here.
admin.site.register(Setting)
admin.site.register(Contact)
admin.site.register(Gallery)
admin.site.register(FAQ)
admin.site.register(News)
admin.site.register(Promotion)
admin.site.register(Benefit)
admin.site.register(Team)
admin.site.register(WeAre)
admin.site.register(Partners)
