import django_filters
from django_filters import CharFilter

from .models import *
from Profile.models import Profile


class TaskFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title',
                       lookup_expr='icontains', label="Title")

    class Meta:
        model = Task
        fields = ['given_to', 'deadline']


class UserTaskFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title',
                       lookup_expr='icontains', label="Title")

    class Meta:
        model = Task
        fields = ['deadline']


class MeetingFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name',
                      lookup_expr='icontains', label="Name")

    class Meta:
        model = Meeting
        fields = ['type', 'category', 'meeting_date']


class ReportFilter(django_filters.FilterSet):
    class Meta:
        model = TaskReport
        fields = ['created_by', 'given_to']


class ProfileFilter(django_filters.FilterSet):
    first_name = CharFilter(field_name='first_name',
                            lookup_expr='icontains', label="Name")

    class Meta:
        model = Profile
        fields = ['position']
