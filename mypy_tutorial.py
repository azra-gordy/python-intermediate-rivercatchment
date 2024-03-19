flag: bool = True


def greet(name: str) -> None:
    """Say hello to everyone"""
    print("Hi " + name)


greet("Manchester")


def greetAll(names: list[str]) -> None:
    for name in names:
        print('Hello ' + name)


greetAll(["Alice", "Baiba", "Cornelius"])
# Lists are homogenous - they need to all be of the same type

# This will return an error:
#greetAll(["Azra", "Stanislav", 55])


some_data: tuple[int, bool, str] = (42, True, "Manchester")
# Tuples can have different types declared

x: dict[str, float] = {"field1": 2.0, "field2": 3.0}
# Dictionaries map a key to a value

# Python will allow you to create tuples/dictionaries with multiple types - in these
# cases MyPy is being more restrictive about what types you can have


def myDiv(x: float, y: float) -> (float | None):
    if y!= 0: return x / y
    else: return None
# Union types (written "t1 | t2") can be used to capture instances where there may be
# more than one type depending on the situation


myDict: dict[str, float | str] = {"temp": 273.0, "units": "Kelvin"}
# ^ Using union to declare multiple types in a dictionary

# reveal_type(myDict)
# MyPy can provide information back - it can also be used to query wider python things:
# reveal_type(len)

# The above will return errors if running the program - need to import to be able to
# run the code:

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    reveal_type(len)

# List is a subtype of Iterable - you can use the higher level type to allow the function
# to take in other parent types:

from typing import Iterable


def greetAllIt(names: Iterable[str]) -> None:
    for name in names:
        greet(name)


# This will work:
greetAllIt({"hi": 42, "test": 55})
# This will throw an error:
# greetAll({"hi": 42, "test": 55})

# Parametric polymorphism:

from typing import Any, TypeVar

# For the following function the actual type doesn't matter - but
# using generic type 'Any' doesn't give much information about the function

def first_worse(xs: list[Any]) -> Any:
    return xs[0]

# Instead you can declare a generic type variable and specify that the input
# has to be a list of the type variable and the output is of the same type

T = TypeVar('T')


def first(xs: list[T]) -> T:
    return xs[0]

from typing import Callable

S = TypeVar('S')

def memo(f: Callable[[S], T], x: S) -> tuple[S, T]:
    return (x, f(x))

# Most type checkers are incomplete, which means they will reject some valid
# programs that can't be coded with their typing system - so Python has an
# escape hatch:
borked = 0 / "hello"  # type: ignore

# MyPy and NumPy

import numpy.typing as npt