import pytest

from string_utils import count_vowels, is_palindrome, reverse_words


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("hello world", "world hello"),
        ("", ""),
        ("  hello   world  ", "world hello"),
        ("one", "one"),
    ],
)
def test_reverse_words(text, expected):
    assert reverse_words(text) == expected


def test_reverse_words_invalid_type():
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_words(None)


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("OpenAI", 4),
        ("rhythms", 0),
        ("", 0),
    ],
)
def test_count_vowels(text, expected):
    assert count_vowels(text) == expected


def test_count_vowels_invalid_type():
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels(123)


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("level", True),
        ("A man, a plan, a canal: Panama", True),
        ("hello", False),
        ("", True),
    ],
)
def test_is_palindrome(text, expected):
    assert is_palindrome(text) is expected


def test_is_palindrome_invalid_type():
    with pytest.raises(TypeError, match="Input must be a string"):
        is_palindrome(["n", "o", "o", "n"])
