from django.contrib.auth import get_user_model

from db.models import User


def get_user(user_id: int) -> User:
    return get_user_model().objects.get(id=user_id)


def create_user(
        username: str,
        password: str,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
) -> User:
    return get_user_model().objects.create_user(
        username=username,
        password=password,
        email=email if email else "",
        first_name=first_name if first_name else "",
        last_name=last_name if last_name else "",
    )


def update_user(
        user_id: int,
        username: str = None,
        password: str = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
) -> None:
    user = get_user_model().objects.get(id=user_id)

    if username:
        user.username = username
    if password:
        user.set_password(password)
    if email:
        user.email = email
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name

    user.save()
