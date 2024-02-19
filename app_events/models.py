from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    owner = models.ForeignKey(User, related_name='owned_events',
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    max_attendees = models.PositiveIntegerField(default=10, blank=True)

    def __str__(self):
        return self.name


class Registration(models.Model):
    event = models.ForeignKey(Event, related_name='registrations', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='event_registrations', on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [('event', 'user')]

    def __str__(self):
        return f'{self.user.username} registered for {self.event.name}'
