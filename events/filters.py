import django_filters
from django.utils import timezone
from .models import Event


class EventFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    start_date_after = django_filters.DateTimeFilter(field_name='start_date', lookup_expr='gte')
    end_date_before = django_filters.DateTimeFilter(field_name='end_date', lookup_expr='lte')
    upcoming = django_filters.BooleanFilter(method='filter_upcoming_events', label='Upcoming Events')
    past = django_filters.BooleanFilter(method='filter_past_events', label='Past Events')

    class Meta:
        model = Event
        fields = ['name', 'start_date_after', 'end_date_before', 'max_attendees']

    def filter_upcoming_events(self, queryset, name, value):
        if value:
            return queryset.filter(start_date__gte=timezone.now())
        return queryset

    def filter_past_events(self, queryset, name, value):
        if value:
            return queryset.filter(end_date__lt=timezone.now())
        return queryset
