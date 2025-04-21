"""Basic types example."""

from mytypes import User

user: User = {
    "name": "Jhon",
    "email": "jhon@testingemail.com",
    "id": 1,
    "phone": "+1234567890",
}

print("Init user", user)


def change_name(name: str) -> User:
    """_summary_.

    Args:
        name (str):New name asignation

    Returns:
        user: user of User type.
    """
    user["name"] = name
    return user


print(change_name("charles"))
