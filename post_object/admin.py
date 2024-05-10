from django.contrib import admin

from . import models
# Register your models here.

class post_show(admin.ModelAdmin):
    list_display=['id']


admin.site.register(models.Post,post_show)
admin.site.register(models.Coments)