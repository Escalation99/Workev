from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, date

# Create your models here.


class Meeting(models.Model):
    created_by = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)

    LIST_TYPE = {
        ('Online', 'Online'),
        ('Regular', 'Regular'),
        ('Seminar', 'Seminar'),
    }
    type = models.CharField(
        max_length=255, choices=LIST_TYPE, default="Regular")
    content = models.TextField()
    room = models.CharField(max_length=255)
    meeting_date = models.DateField("Date (mm/dd/yyyy)",
                                    auto_now_add=False, auto_now=False, default=timezone.now, blank=True, null=True)
    meeting_time = models.TimeField("Time (hh:mm)",
                                    auto_now=False, auto_now_add=False, default=timezone.now, blank=True, null=True)

    LIST_CATEGORY = {
        ('Sprint Planning', 'Sprint Planning'),
        ('Code Review', 'Code Review'),
        ('Sprint Retrospective', 'Sprint Retrospective'),
        ('Alignment Meeting', 'Alignment Meeting'),
        ('Regular Meeting', 'Regular Meeting'),
    }
    category = models.CharField(
        max_length=50, choices=LIST_CATEGORY, default="Regular Meeting")

    LIST_DIVISION = {
        ('CEO', 'CEO'),
        ('Vice CEO', 'Vice CEO'),
        ('Scrum Master', 'Scrum Master'),
        ('Project Manager', 'Project Manager'),
        ('Fullstack Developer', 'Fullstack Developer'),
        ('Frontend Developer', 'Frontend Developer'),
        ('Backend Developer', 'Backend Developer'),
        ('UI/UX Designer', 'UI/UX Designer'),
        ('Junior Developer', 'Junior Developer'),
        ('Intern', 'Intern'),
        ('All', 'All'),

    }
    division = models.CharField(
        max_length=50, choices=LIST_DIVISION, default="All")
    created_at = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(null=True, blank=True)
    finished = models.BooleanField(default=False, blank=False)

    def save(self):
        super().save()

    def __str__(self):
        return "{}. {}".format(self.id, self.name)

    class Meta:
        unique_together = [("meeting_date", "room")]


class Task(models.Model):
    created_by = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="task_sender")
    given_to = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="task_receiver")
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(null=True, blank=True)
    status = models.CharField(max_length=20, default="new")
    deadline = models.DateField("Deadline (mm/dd/yyyy)",
                                auto_now_add=False, auto_now=False, default=timezone.now, blank=True, null=True)

    def save(self):
        super().save()

    def __str__(self):
        return "{} - {}".format(self.id, self.title)


class SubTask(models.Model):
    belongs_to = models.ForeignKey(
        Task, null=True, on_delete=models.CASCADE, related_name="subtask_set")
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    finished = models.BooleanField(default=False, blank=False)
    given_to = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE)

    def save(self):
        super().save()

    def __str__(self):
        return "{} - {}".format(self.id, self.title)


class TaskReport(models.Model):
    task = models.ForeignKey(
        Task, null=True, on_delete=models.CASCADE, related_name="report_user")
    created_by = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="sender")
    given_to = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="receiver")
    comments = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(null=True, blank=True)

    def save(self):
        super().save()

    def __str__(self):
        return "{} - {}".format(self.id, self.comments)


class ReportFeedback(models.Model):
    report = models.ForeignKey(
        TaskReport, null=True, on_delete=models.CASCADE, related_name="report_feedback")
    created_by = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="feedback_sender")
    given_to = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="feedback_receiver")
    comments = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(null=True, blank=True)

    def save(self):
        super().save()

    def __str__(self):
        return "{} - {}".format(self.id, self.comments)


class Attendance(models.Model):
    user = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="attendance_user")
    clock_in = models.DateTimeField(auto_now_add=True)
    clock_out = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default="Absent")

    def save(self):
        super().save()

    def __str__(self):
        return "{} - {}".format(self.id, self.status)


class Feedback(models.Model):
    created_by = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="app_feedback_sender")
    given_to = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="app_feedback_receiver")
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self):
        super().save()

    def __str__(self):
        return "{} - {}".format(self.id, self.title)


class FeedbackReply(models.Model):
    created_by = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="app_feedback_reply_sender")
    given_to = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="app_feedback_reply_receiver")
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self):
        super().save()

    def __str__(self):
        return "{} - {}".format(self.id, self.title)


class Notification(models.Model):
    created_by = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="notification_sender")
    given_to = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="notification_receiver")
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False, blank=False)

    def save(self):
        super().save()

    def __str__(self):
        return "{} - {}".format(self.id, self.title)


class PaidLeave(models.Model):
    created_by = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="paid_leave_sender")
    given_to = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="paid_leave_receiver")
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(null=True, blank=True)
    status = models.CharField(max_length=20, default="Pending")

    def save(self):
        super().save()

    def __str__(self):
        return "{} - {}".format(self.id, self.title)


class TaskReportHistory(models.Model):
    task = models.ForeignKey(
        Task, null=True, on_delete=models.CASCADE, related_name="report_history")
    created_by = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="history_sender")
    given_to = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="history_receiver")
    comments = models.TextField()
    attachment = models.FileField(null=True, blank=True)

    def save(self):
        super().save()

    def __str__(self):
        return "{} - {}".format(self.id, self.comments)
