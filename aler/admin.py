from django.contrib import admin
from .models import Property, Property_review, Agent, Photo
# Register your models here.

admin.site.register(Agent)
admin.site.register(Property)
admin.site.register(Photo)
admin.site.register(Property_review)
