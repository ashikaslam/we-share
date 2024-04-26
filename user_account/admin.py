from django.contrib import admin
from. import models
# Register your models here.

class user_admin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','mobile_number']

admin.site.register(models.User,user_admin)
admin.site.register(models.Adrress)
admin.site.register(models.Profile)