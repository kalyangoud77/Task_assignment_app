from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

class TaskAssignment(models.Model):

    PRIORITIES = (
        ('0_low', _('Low')),
        ('1_normal', _('Normal')),
        ('2_high', _('High')),
        ('3_critical', _('Critical')),
        ('4_blocker', _('Blocker'))
    )

    task_name = models.CharField(max_length=50,null=True)
    assigned_to = models.CharField(max_length=50)
    assigned_at = models.DateTimeField(default=timezone.now, blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    descreption = models.TextField(_("Task about"), max_length=2000, null=True, blank=True)
    task_prority = models.CharField(_("priority"), max_length=20, choices=PRIORITIES, default='10_normal')


    def __str__(self):
        return "%s,%s,%s,%s,%s,%s" % (self.assigned_to, self.assigned_at, self.deadline, str(self.task_prority),self.task_name,self.descreption)

class Taskdone(models.Model):

    STATUSES = (
        ('to-do', _('To Do')),
        ('in_progress', _('In Progress')),
        ('blocked', _('Blocked')),
        ('done', _('Done')),
        ('dismissed', _('Dismissed'))
    )

    user_name = models.CharField(max_length=50, null=True)
    taskdone = models.TextField(_("Task done"), max_length=2000, null=True, blank=True)
    assigned_at = models.DateTimeField(default=timezone.now, blank=True, null=True)
    taskdone_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(_("state"), max_length=20, choices=STATUSES, default='to-do')

    def __str__(self):
        return "%s,%s,%s,%s" % (self.user_name,self.assigned_at, self.taskdone_at, self.status)



