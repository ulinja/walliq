"""Common assertions used in sanity checks."""

from pathlib import Path
from string import hexdigits
from typing import Any


def assert_is_int(value: Any) -> None:
    """Asserts that value is an int.

    Args:
        value (Any): The value to check.

    Raises:
        TypeError: If value is not an int.
    """
    if not isinstance(value, int):
        raise TypeError(f"Expected type 'int' but got '{type(value).__name__}'.")


def assert_is_positive_int(value: Any) -> None:
    """Asserts that value is a positive int.

    Args:
        value (Any): The value to check.

    Raises:
        TypeError: If value is not an int.
        ValueError: If value is negative.
    """
    assert_is_int(value)
    if value < 0:
        raise ValueError(f"Expected a positive int but got {value}.")


def assert_is_positive_nonzero_int(value: Any) -> None:
    """Asserts that value is a positive, non-zero int.

    Args:
        value (Any): The value to check.

    Raises:
        TypeError: If value is not an int.
        ValueError: If value is negative or zero.
    """
    assert_is_int(value)
    if not value > 0:
        raise ValueError(f"Expected a positive non-zero int but got {value}.")


def assert_is_path_or_str(value: Any) -> None:
    """Asserts that value is a Path or a str.

    Args:
        value (Any): The value to check.

    Raises:
        TypeError: If value is not a Path or str.
    """
    if not isinstance(value, (Path, str)):
        raise TypeError(f"Expected type 'Path' or 'str' but got '{type(value).__name__}'.")


def assert_is_str(value: Any) -> None:
    """Asserts that value is a str.

    Args:
        value (Any): The value to check.

    Raises:
        TypeError: If value is not a str.
    """
    if not isinstance(value, str):
        raise TypeError(f"Expected type 'str' but got '{type(value).__name__}'.")


def assert_is_nonempty_str(value: Any) -> None:
    """Asserts that value is a nonempty string.

    Args:
        value (Any): The value to check.

    Raises:
        TypeError: If value is not a str.
        ValueError: If value is an empty string.
    """
    assert_is_str(value)
    if not value:
        raise ValueError("Expected a nonempty string but got an empty string.")


def assert_is_hexadecimal_color_str(value: Any) -> None:
    """Asserts that value is a hexadecimal color string.

    A valid hexadecimal color string has the format #[0-9A-Fa-f]{6}

    Args:
        value (Any): The value to check.

    Raises:
        TypeError: If value is not a str.
        ValueError: If value is not in a valid hexadecimal color format.
    """
    assert_is_nonempty_str(value)

    def _fail():
        raise ValueError(f"Expected a hexadecimal color string but got '{value}'.")

    if not value.startswith("#"):
        _fail()
    hex_chars = value[1:]
    if len(hex_chars) != 6:
        _fail()
    for char in hex_chars:
        if char not in hexdigits:
            _fail()
