from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    created_by = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()

    LIST_CATEGORY = {
        ('Jobdesc', 'Jobdesc'),
        ('Meeting', 'Meeting'),
        ('Announcement', 'Announcement'),
        ('Other', 'Other'),

    }
    category = models.CharField(
        max_length=50, choices=LIST_CATEGORY, default="Jobdesc")
    created_at = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(null=True, blank=True)

    def save(self):
        super().save()

    def __str__(self):
        return "{}. {}".format(self.id, self.title)


class Reply(models.Model):
    created_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    replied_to = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, default="reply")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(null=True, blank=True)

    def save(self):
        super().save()

    def __str__(self):
        return "{} - {}".format(self.id, self.created_by)
