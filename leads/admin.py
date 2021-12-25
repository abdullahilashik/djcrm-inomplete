from django.contrib import admin
from .models import Agent, Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'agent']


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    pass
