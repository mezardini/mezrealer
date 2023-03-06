from django.contrib import admin
from .models import Property,  Agent, Photo
# Register your models here.

admin.site.register(Agent)
admin.site.register(Property)
admin.site.register(Photo)

