from django.contrib import admin
from .models import ImageModel, RegistrationModel, EventModel

admin.site.register(RegistrationModel)
admin.site.register(EventModel)
admin.site.register(ImageModel)