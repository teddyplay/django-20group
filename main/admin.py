from django.contrib import admin
from . import models


admin.site.register(models.Film)
admin.site.register(models.Rewiev)
admin.site.register(models.FilmComment)

