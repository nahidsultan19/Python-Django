import django_filters
from .models import *


class SongsFilter(django_filters.FilterSet):
    class Meta:
        model = Songs
        fields = ['title', 'band']
