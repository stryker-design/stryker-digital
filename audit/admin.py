from django.contrib import admin

from audit.models import *

# Register your models here.

@admin.register(Audit)
class AuditAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('business_name',)}