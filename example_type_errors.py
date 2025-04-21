"""Example file demonstrating Python type errors that static type checkers should detect.
This file intentionally contains type errors to show how linters and type checkers work.
NOTE: This file is meant to be ignored by pre-commit hooks for demonstration purposes.
"""
from typing import Dict, List, TypedDict, Union


class User(TypedDict):
    """User data structure with type information."""

    name: str
    email: str
    id: int
    active: bool
    phone: str


# Example 1: Missing type annotations
missing_type = "This variable has no type annotation"
valid_variable: str = "This variable has proper type annotation"

# Example 2: TypedDict usage with incorrect types
user: User = {
    "name": "John Smith",
    "email": "john@example.com",
    "id": 123,
    "active": True,
    "phone": "+1234567890",
}

# Type error: assigning int to a string field
user["email"] = 42


# Example 3: Function with incorrect parameter types
def add_numbers(a: int, b: int) -> int:
    return a + b


# Type error: passing string to a function expecting int
result = add_numbers("hello", 5)


# Example 4: Function with missing return type
def multiply(a: int, b: int):  # Missing return type
    return a * b


# Example 5: Function with incorrect return type
def get_username(user_data: User) -> int:
    return user_data["name"]  # Returns str, but declared to return int


# Example 6: Incorrect list usage
names: List[str] = ["Alice", "Bob", "Charlie"]
names.append(42)  # Type error: adding int to List[str]


# Example 7: Parameter without type annotation
def process_data(data: List[int], factor):  # 'factor' missing type
    return [x * factor for x in data]


# Example 8: Inconsistent variable types
counter: int = 10
counter = "ten"  # Type error: assigning str to int variable


# Example 9: Optional parameters handling
def greet(name: str, formal: bool = False) -> str:
    if formal:
        return f"Good day, {name}"
    return f"Hey, {name}!"


greet(123)  # Type error: passing int where str is expected

# Example 10: Complex nested types
users_by_department: Dict[str, List[User]] = {
    "Engineering": [user],
    "Marketing": 123,  # Type error: should be List[User]
}


# Example 11: Union types
def process_id(user_id: Union[int, str]) -> str:
    return str(user_id)


process_id([1, 2, 3])  # Type error: list is not Union[int, str]


# Example 12: Missing docstring (if configured to check)
def calculate_total(items: List[float]) -> float:
    return sum(items)


print("This example file shows common type errors that should be detected.")
