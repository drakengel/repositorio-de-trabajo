from django.contrib import admin
from .models import Portfolio

# Create your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')



admin.site.register(Portfolio, ProjectAdmin)
# Register your models here.
