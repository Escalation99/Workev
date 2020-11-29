from django.db import models
from django.contrib.auth.models import User
#from django.utils.text import slugify

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile_user")
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    address = models.TextField()
    employeeSince = models.DateTimeField(auto_now_add=True)
    lastDataUpdate = models.DateTimeField(auto_now=True)
    salary = models.CharField(max_length=50, default="undefined")

    LIST_POSITION = {
        ('Vice CEO', 'Vice CEO'),
        ('Scrum Master', 'Scrum Master'),
        ('Project Manager', 'Project Manager'),
        ('Fullstack Developer', 'Fullstack Developer'),
        ('Frontend Developer', 'Frontend Developer'),
        ('Backend Developer', 'Backend Developer'),
        ('UI/UX Designer', 'UI/UX Designer'),
        ('Junior Developer', 'Junior Developer'),
        ('Intern', 'Intern'),
    }
    position = models.CharField(
        max_length=50, choices=LIST_POSITION, default="Junior Developer")
    profile_pic = models.ImageField(
        default="social.png", null=True, blank=True)

    def __str__(self):
        return "{}'s Profile".format(self.first_name)
