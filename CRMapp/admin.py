from django.contrib import admin
from .models import Auto, User, Lead, Agent, Category

admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)
admin.site.register(Auto)
admin.site.register(Category)
