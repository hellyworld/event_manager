import pytest

pytestmark = pytest.mark.django_db()


class TestEventModel:
    def test_str_method(self, event_factory):
        event = event_factory(name="Event no 0")
        assert event.__str__() == "Event no 0"


class TestRegistrationModel:
    def test_str_method(self, registration_factory):
        registration = registration_factory()
        expected_str = (
            f"{registration.user.username} registered for {registration.event.name}"
        )
        assert registration.__str__() == expected_str
