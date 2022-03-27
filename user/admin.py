from django.contrib import admin

from user.models import Appointment, Blog, Profile

# Register your models here.


admin.site.register(Profile)
admin.site.register(Blog)
admin.site.register(Appointment)