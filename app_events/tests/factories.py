import datetime
import random

import factory
from django.utils import timezone

from app_events.models import Event, Registration, User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.Sequence(lambda n: f"user{n}@example.com")


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    owner = factory.SubFactory(UserFactory)
    name = factory.Sequence(lambda n: f"Event no {n}")
    description = factory.Sequence(lambda n: f"Event no {n} description")
    start_date = factory.LazyFunction(
        lambda: timezone.now() + datetime.timedelta(days=random.randint(1, 3))
    )
    end_date = factory.LazyFunction(
        lambda: timezone.now() + datetime.timedelta(days=random.randint(4, 5))
    )
    max_attendees = factory.LazyFunction(lambda: random.randint(1, 50))


class RegistrationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Registration

    event = factory.SubFactory(EventFactory)
    user = factory.SubFactory(UserFactory)
    registration_date = factory.LazyFunction(lambda: timezone.now())
