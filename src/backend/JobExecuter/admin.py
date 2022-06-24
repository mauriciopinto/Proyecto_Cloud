from django.contrib import admin
from JobExecuter.models import ExecutedJob, Status

# Register your models here.
@admin.register(ExecutedJob)
class ExecutedJobAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'job_id', 'execution_time', 'status', 'running_time')


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_status')