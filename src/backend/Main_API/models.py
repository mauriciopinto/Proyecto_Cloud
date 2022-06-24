from enum import unique
from tabnanny import verbose
from django.db import models
from django.http import request

# Create your models here.
class User(models.Model):
    username = models.CharField(
        max_length=30,
        unique=True
    )

    password = models.CharField(
        max_length=60,
        editable=True
    )

    email = models.EmailField(
        max_length=254,
        unique=True
    )

    client_id = models.ForeignKey (
        to='Client',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['client_id']
        verbose_name = 'user'
        verbose_name_plural = 'users'
        app_label = 'Main_API'


class Job(models.Model):
    name = models.CharField (
        max_length=100,
        null=False,
        blank=False
    )

    description = models.TextField (
        blank=True
    )

    path = models.CharField (
        max_length=255,
        blank=False
    )

    input_type = models.ManyToManyField(
        to='FileType',
        related_name='input_types'
    )

    input_amount = models.IntegerField (
        null=False,
        blank=False,
        default=1
    )

    output_type = models.ManyToManyField(
        to='FileType',
        related_name='output_types'
    )

    client_id = models.ForeignKey(
        to='Client',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['client_id']
        verbose_name = 'job'
        verbose_name_plural = 'jobs'
        app_label = 'Main_API'


class Client(models.Model):
    business_name = models.CharField(
        max_length=100,
        unique=True
    )

    ruc = models.CharField(
        max_length=11,
        unique=True
    )

    payment_date = models.DateField()

    contact_email = models.EmailField(
        max_length=254,
        unique=True
    )

    contact_phone = models.CharField(
        max_length=12
    )

    def __str__(self):
        return self.business_name

    class Meta:
        ordering = ['id']
        verbose_name = 'client'
        verbose_name_plural = 'clients'
        app_label = 'Main_API'


class FileType(models.Model):
    file_extension = models.CharField(
        max_length=8
    )

    def __str__(self):
        return self.file_extension

    class Meta:
        ordering = ['id']
        verbose_name = 'file type'
        verbose_name_plural = 'file types'
        app_label = 'Main_API'

class Argument(models.Model):
    job_id = models.ForeignKey(
        to='Job',
        on_delete=models.CASCADE
    )

    arg_type = models.CharField(
        max_length=20,
        blank=False
    )

    placeholder = models.CharField(
        max_length=20,
        blank=False
    )

    def __str__(self):
        return self.placeholder

    class Meta:
        ordering = ['id']
        verbose_name = 'argument'
        verbose_name_plural = 'arguments'
        app_label = 'Main_API'