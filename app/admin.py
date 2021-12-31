from django.contrib import admin
from .models import RegistrationModel, EventModel

admin.site.register(RegistrationModel)
admin.site.register(EventModel)