from enum import Enum
from typing import TypeVar, Tuple, cast

T = TypeVar("T", bound="EnhancedEnum")


class EnhancedEnum(Enum):
    """
    A generic, enhanced enumeration class providing additional convenience methods.

    `EnhancedEnum` extends the standard Python Enum class, adding methods for more user-friendly string representation,
    listing all enum members, validating members, cycling through members, and creating members from strings or values.
    It utilizes generics to ensure that methods return the correct specific enum type.

    Attributes:
        Enum members (various): Defined as class attributes with unique values.

    Methods:
        __str__: Returns a user-friendly string representation of the enum member.
        list_all: Returns a list of all enum members.
        validate: Checks if a given value is a valid member of the enum.
        as_tuple: Returns the enum members as a tuple.
        next: Returns the next enum member in sequence.
        previous: Returns the previous enum member in sequence.
        from_string: Returns the corresponding enum member for a given name.
        from_value: Returns the corresponding enum member for a given numeric value.

    Example:
        ```python
        from enum import auto

        class Color(EnhancedEnum):
            RED = auto()
            GREEN = auto()
            BLUE = auto()

        # List all members
        print(Color.list_all())

        # Validate a member
        print(Color.validate(Color.RED))

        # Get next and previous members
        print(Color.RED.next())
        print(Color.RED.previous())

        # Create a member from a string
        print(Color.from_string('RED'))

        # Create a member from a value
        print(Color.from_value(1))
        ```
    """
    def __str__(self) -> str:
        """
        Return a more user-friendly string representation of the enum member.

        Overrides the default __str__ method to return the name of the enum member instead of its Enum class and name.

        Returns:
            str: The name of the enum member.
        """
        return self.name

    @classmethod
    def list_all(cls: type[T]) -> list[T]:
        """
        Return a list of all enum members.

        Provides a convenient way to list all members of the enum class.

        Returns:
            list[T]: A list containing all members of the enum class.
        """
        return cast(list[T], list(cls))

    @classmethod
    def validate(cls, value) -> bool:
        """
        Check if the provided value is a valid member of the enum.

        Args:
            value: The value to check.

        Returns:
            bool: True if the value is a valid member, False otherwise.
        """
        return value in cls._value2member_map_

    @classmethod
    def as_tuple(cls: type[T]) -> Tuple[T, ...]:
        """
        Return the enum members as a tuple.

        Provides a convenient way to get all members of the enum class in a tuple form.

        Returns:
            Tuple[T, ...]: A tuple containing all members of the enum class.
        """
        return cast(Tuple[T, ...], tuple(member for member in cls))

    def next(self: T) -> T:
        """
        Return the next enum member in sequence.

        If the current member is the last, it returns the first member.

        Returns:
            T: The next enum member in sequence.
        """
        members = list(self.__class__)
        index = members.index(self) + 1
        if index >= len(members):
            index = 0
        return members[index]

    def previous(self: T) -> T:
        """
        Return the previous enum member in sequence.

        If the current member is the first, it returns the last member.

        Returns:
            T: The previous enum member in sequence.
        """
        members = list(self.__class__)
        index = members.index(self) - 1
        if index < 0:
            index = len(members) - 1
        return members[index]

    @classmethod
    def from_string(cls: type[T], name: str) -> T:
        """
        Return the corresponding enum member for a given name.

        Args:
            name (str): The name of the member to retrieve.

        Returns:
            T: The corresponding enum member.

        Raises:
            ValueError: If the name does not correspond to any member.
        """
        try:
            return cast(T, cls[name])
        except KeyError:
            raise ValueError(f"{name} is not a valid member name")

    @classmethod
    def from_value(cls: type[T], value: int) -> T:
        """
        Return the corresponding enum member for a given numeric value.

        Args:
            value (int): The numeric value of the member to retrieve.

        Returns:
            T: The corresponding enum member.

        Raises:
            ValueError: If the value does not correspond to any member.
        """
        for member in cls:
            if member.value == value:
                return cast(T, member)
        raise ValueError(f"{value} is not a valid member value")
