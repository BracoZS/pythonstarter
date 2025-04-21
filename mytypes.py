"""Basic types exportation."""
from typing import Dict, List, Optional, TypedDict, TypeVar, Union

# Basic type aliases
StrOrInt = Union[str, int]
OptionalStr = Optional[str]
IntList = List[int]
StrDict = Dict[str, str]

# Generic type variable
T = TypeVar("T")

# Example complex type
JsonData = Union[Dict[str, "JsonData"], List["JsonData"], str, int, float, bool, None]


class User(TypedDict):
    """_summary_.

    Args:
        TypedDict (_type_): _description_
    """

    name: str
    phone: str
    email: str
    id: int
