from datetime import timedelta

from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from app_events.models import Event


class EventFilterTests(APITestCase):
    def setUp(self):
        # Create a user for ownership of app_events
        self.user = User(username='testuser', password='testpassword')

        # Create some app_events for testing
        self.event_past = Event(
            owner=self.user,
            name="Past Event",
            description="This event has already happened.",
            start_date=timezone.now() - timedelta(days=2),
            end_date=timezone.now() - timedelta(days=1),
            max_attendees=50
        )
        self.event_upcoming = Event(
            owner=self.user,
            name="Upcoming Event",
            description="This event is in the future.",
            start_date=timezone.now() + timedelta(days=1),
            end_date=timezone.now() + timedelta(days=2),
            max_attendees=50
        )

    def test_filter_upcoming_events(self):
        """
        Ensure we can filter app_events to show only upcoming ones.
        """
        url = reverse('event-list')
        response = self.client.get(url, {'upcoming': 'true'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response contains only upcoming app_events
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.event_upcoming.name)