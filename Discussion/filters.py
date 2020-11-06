import django_filters
from django_filters import CharFilter

from .models import *


class PostFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title',
                       lookup_expr='icontains', label="Title")

    class Meta:
        model = Post
        fields = ['created_by', 'category']
