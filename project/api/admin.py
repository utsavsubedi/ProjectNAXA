from django.contrib import admin
from api.models import Address, Budget, Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ( 'project_title', 'project_status', 'donor')
    list_filter = ( 'project_title', 'project_status', 'donor')

class BudgetAdmin(admin.ModelAdmin):
    list_display = ('budget_type', 'commitments')
    list_filter = ( 'budget_type',)

class AdressAdmin(admin.ModelAdmin):
    list_display = ('province', 'district', 'municipality', 'project', 'budget')
    list_filter = ('province', 'district', 'municipality', 'project')

admin.site.register(Address, AdressAdmin)
admin.site.register(Budget, BudgetAdmin)
admin.site.register(Project, ProjectAdmin)