from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Schedule


class ScheduleResource(resources.ModelResource):
    class Meta:
        model = Schedule

@admin.register(Schedule)
class ScheduleAdmin(ImportExportModelAdmin):
    ordering = ['id']
    list_display=('id', 'date', 'time', 'name', 'num_of_people', 'tel_number', 'memo')

    resource_class = ScheduleResource

