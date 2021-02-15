from django.contrib import admin
from institution.models import News, SacredDates, GenericPage


admin.site.register(News)
admin.site.register(SacredDates)
admin.site.register(GenericPage)