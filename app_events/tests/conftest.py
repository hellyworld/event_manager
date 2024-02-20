import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from app_events.tests.factories import (
    EventFactory,
    RegistrationFactory,
    UserFactory,
)

register(EventFactory)
register(UserFactory)
register(RegistrationFactory)


@pytest.fixture
def api_client():
    return APIClient
