"""Example file demonstrating correct Python type annotations and usage."""

from typing import Dict, List, Optional, TypedDict, Union


class User(TypedDict):
    """User data structure with type information."""

    name: str
    email: str
    id: int
    active: bool
    phone: str


# Example 1: Missing type annotations
valid_variable: str = "This variable has proper type annotation"

# Example 2: TypedDict usage with incorrect types
user: User = {
    "name": "John Smith",
    "email": "john@example.com",
    "id": 123,
    "active": True,
    "phone": "+1234567890",
}

user["email"] = "newEmail@email.com"


# Example 3: Function with incorrect parameter types
def add_numbers(a: int, b: int) -> int:
    """Execute a sum of given numbers.

    Args:
        a (int):number
        b (int): number

    Returns:
        int: The sum of given numbers
    """
    return a + b


RESULT = add_numbers(4, 5)


# Example 4: Function with correct return type
def multiply(a: int, b: int) -> int:
    """Execute a multiply of given numbers.

    Args:
        a (int): Number
        b (int): Number

    Returns:
        int: Multiply result
    """
    return a * b


# Example 5: Function with correct return type
def get_username(user_data: User) -> str:
    """Get name of user dict.

    Args:
        user_data (User): User Data dictionary

    Returns:
        str: name
    """
    return user_data["name"]


# Example 6: Correct list usage
names: List[str] = ["Alice", "Bob", "Charlie"]
names.append("Maria")


# Example 7: Parameter with type annotation
def process_data(data: List[int], factor: int) -> List[int]:
    """Generate a new list multiply each element with given factor.

    Args:
        data (List[int]): Array of numbers
        factor (int): Multiply factor

    Returns:
        List[int]: New list
    """
    return [x * factor for x in data]


# Example 8: Consistent variable types
COUNTER: int = 10


# Example 9: Optional parameters handling
def greet(name: Optional[str] = None, formal: Optional[bool] = None) -> str:
    """Example of function with optional parameters.

    Args:
        name (Optional[str], optional): _description_. Defaults to None.
        formal (Optional[bool], optional): _description_. Defaults to None.

    Returns:
        str: Message.
    """
    if formal:
        return f"Good day, {name}"
    return f"Hey, {name}!"


greet()

# Example 10: Complex nested types
users_by_department: Dict[str, List[User]] = {
    "Engineering": [user],
    "Marketing": [user],
}


# Example 11: Union types
def process_id(user_id: Union[int, str]) -> str:
    """Example of union type.

    Args:
        user_id (Union[int, str]): _description_

    Returns:
        str: Transformed input parameter to string
    """
    return str(user_id)


process_id(1)
process_id("1")
