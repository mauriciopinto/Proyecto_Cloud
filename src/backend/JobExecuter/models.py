from django.db import models
from Main_API.models import User, Job, Client

# Create your models here.
class ExecutedJob(models.Model):
    tagname = models.CharField (
        max_length=60,
        default="jobname"
    )

    job_id = models.ForeignKey(
        to='Main_API.Job',
        on_delete=models.CASCADE
    )

    user_id = models.ForeignKey(
        to='Main_API.User',
        on_delete=models.CASCADE
    )

    execution_time = models.DateTimeField (
        auto_now=True
    )

    status = models.ForeignKey (
        to='Status',
        on_delete=models.CASCADE,
        default=1
    )

    output = models.CharField (
        max_length=255,
        default="",
        null=True
    )

    running_time = models.FloatField (
        default=0.0
    )

    def __str__(self):
        return self.tagname

    class Meta:
        ordering = ['user_id']
        verbose_name = 'executed job'
        verbose_name_plural = 'executed jobs'
        app_label = 'JobExecuter'

class Status(models.Model):
    job_status = models.CharField (
        max_length=20
    )

    def __str__(self):
        return self.job_status

    class Meta:
        ordering = ['id']
        verbose_name = 'status'
        verbose_name_plural = 'statuses'
        app_label = 'JobExecuter'