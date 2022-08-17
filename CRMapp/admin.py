from django.contrib import admin
from .models import Organisation, User, Lead, Agent

admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)
admin.site.register(Organisation)
