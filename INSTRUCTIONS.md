# Event Manager REST API Specification

The task consists of creating a REST API using [Django Rest Framework](https://www.django-rest-framework.org/) to create an Event Manager app. It should allow users to create a personal account, log in, and create, edit, fetch, and register to attend events. Each event should have at least a name, a description, a start date, an end date, and a list of attendees.

## Required Features

- Users must be able to register an account.
- Users must be able to log in to their account.
- A system of token rotation must be implemented. For this, the API needs to provide a user with `access_token` and a `refresh_token`, as well as a way to refresh and validate the `access_token`. The lifetime of the `access_token` should be 1 hour, and the lifetime of the `refresh_token` should be 1 day.
- Users must be able to create events in the app's database (SQLite).
- Users must be able to see the list of events they have created.
- Users must be able to see a list of all events.
- Users must be able to edit the events they have created but not the ones created by other users.
- Users must be able to register for an event or unregister. This can only be done in future events and not in past events.

## Not Required but Nice to Have

- Documentation of your code.
- API docs (Swagger or other).
- Tests.
- Add logic to manage an event capacity: if the event reaches the maximum number of registered attendees, an error should be returned to a user trying to register.
- Add some filtering to endpoints retrieving events (e.g., date, type, status, past events, future events, etc.).
- Create a frontend to consume the API.

## Delivery

Please use Git. You can choose whatever Git platform you want (Github, Bitbucket, Gitlab, etc).
