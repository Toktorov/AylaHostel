from django.contrib import admin
from apps.settings.models import Setting,Partners, Contact, Reservation, Gallery, FAQ, News, Promotion, Benefit, Team,WeAre
from apps.rooms.models import  Review
# Register your models here.
admin.site.register(Setting)
admin.site.register(Contact)
admin.site.register(Reservation)
admin.site.register(Review)
admin.site.register(Gallery)
admin.site.register(FAQ)
admin.site.register(News)
admin.site.register(Promotion)
admin.site.register(Benefit)
admin.site.register(Team)
admin.site.register(WeAre)
admin.site.register(Partners)
