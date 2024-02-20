import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db()


class TestEventsEndpoints:
    event_endpoint = "/api/events/"

    def test_events_get(self, event_factory, api_client):
        event_factory.create_batch(4)
        response = api_client().get(self.event_endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 4
