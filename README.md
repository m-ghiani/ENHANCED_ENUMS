
# EnhancedEnum

`EnhancedEnum` is a generic, enhanced enumeration class that extends the functionality of Python's standard `Enum` class. It provides additional convenience methods for a more user-friendly approach to handling enumerations. This class utilizes Python's generics to ensure type safety and clarity.

## Features

- **User-Friendly String Representation**: Override the `__str__` method to return the name of the enum member.
- **Listing Members**: Easily list all members of the enumeration.
- **Validation**: Check if a given value is part of the enumeration.
- **Tuple Conversion**: Convert enum members into a tuple.
- **Navigation**: Navigate to the next or previous enum members in sequence.
- **Creation from String**: Instantiate an enum member from its string name.
- **Creation from Value**: Instantiate an enum member from its value.

## Installation

You can copy the `EnhancedEnum` class code into your project, or import it if you've saved it as a separate Python file.

## Usage

Below is an example of how you might define and use the `EnhancedEnum`:

```python
from enum import Enum, auto
from enhanced_enum import EnhancedEnum

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

## Methods

- `__str__`: Return a more user-friendly string representation of the enum member.
- `list_all`: Return a list of all enum members.
- `validate`: Check if a given value is a valid member of the enum.
- `as_tuple`: Return the enum members as a tuple.
- `next`: Return the next enum member in sequence.
- `previous`: Return the previous enum member in sequence.
- `from_string`: Return the corresponding enum member for a given name.
- `from_value`: Return the corresponding enum member for a given numeric value.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/m-ghiani/ENHANCED_ENUMS/issues) if you want to contribute.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Massimo Ghiani - [m.ghiani@gmail.com](mailto:m.ghiani@gmail.com)

Project Link: [https://github.com/m-ghiani/ENHANCED_ENUMS](https://github.com/m-ghiani/ENHANCED_ENUMS)
