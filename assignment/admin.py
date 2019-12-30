from django.contrib import admin
from .models import *

admin.site.register(TaskAssignment)
admin.site.register(Taskdone)
readonly_fields = ('assigned_to','assigned_at', 'deadline')
