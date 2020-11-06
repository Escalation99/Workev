from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Meeting)
admin.site.register(TaskReport)
admin.site.register(ReportFeedback)
admin.site.register(Feedback)
admin.site.register(FeedbackReply)
admin.site.register(Notification)
admin.site.register(PaidLeave)
admin.site.register(TaskReportHistory)
admin.site.register(SubTask)


class attendanceAdmin(admin.ModelAdmin):
    readonly_fields = [
        'clock_in',
        'clock_out',
    ]


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = [
        'deadline',
    ]


admin.site.register(Task, TaskAdmin)
admin.site.register(Attendance, attendanceAdmin)
