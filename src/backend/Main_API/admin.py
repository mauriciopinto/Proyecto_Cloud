from django.contrib import admin
from Main_API.models import Client, FileType, Job, User, Argument

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'client_id')


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'client_id')
    filter_horizontal = ('input_type', 'output_type',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'business_name', 'ruc', 'payment_date', 'contact_email', 'contact_phone')


@admin.register(FileType)
class FileTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_extension')


@admin.register(Argument)
class ArgumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_id', 'arg_type', 'placeholder')