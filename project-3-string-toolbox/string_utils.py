def _validate_string(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("Input must be a string")
    return value


def reverse_words(s: str) -> str:
    """Return the input string with word order reversed."""
    s = _validate_string(s)
    return " ".join(s.split()[::-1])


def count_vowels(s: str) -> int:
    """Count the number of vowels in the input string."""
    s = _validate_string(s)
    vowels = "aeiouAEIOU"
    return sum(char in vowels for char in s)


def is_palindrome(s: str) -> bool:
    """Return True if the input reads the same forwards and backwards.

    The check ignores case and non-alphanumeric characters.
    """
    s = _validate_string(s)
    normalized = "".join(char.lower() for char in s if char.isalnum())
    return normalized == normalized[::-1]
