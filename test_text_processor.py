import pytest
from text_processor import TextProcessor

def test_capitalize_text_equal():
    """1. Assert equal - egyenlőség ellenőrzés"""
    processor = TextProcessor()
    result = processor.capitalize_text("hello world")
    assert result == "HELLO WORLD"

def test_capitalize_text_not_equal():
    """2. Assert not equal - nem egyenlő"""
    processor = TextProcessor()
    result = processor.capitalize_text("hello world")
    assert result != "hello world"


def test_reverse_text_in():
    """3. Assert in - benne van"""
    processor = TextProcessor()
    result = processor.reverse_text("hello")
    assert "olleh" in result
    assert "h" in result
    assert "hello" not in result


def test_reverse_text_not_in():
    """4. Assert not in - nincs benne"""
    processor = TextProcessor()
    result = processor.reverse_text("hello")
    assert "hello" not in result
    assert "world" not in result
    assert "x" not in result


def test_count_words_isinstance():
    """5. Assert isinstance - típus ellenőrzés"""
    processor = TextProcessor()
    result = processor.count_words("This is a test")
    assert isinstance(result, int)
    assert isinstance(processor.count_words("hello world"), int) 


def test_count_words_greater_less():
    """6. Assert >, <, >=, <= - összehasonlítás"""
    processor = TextProcessor()
    result1 = processor.count_words("One two three four")
    result2 = processor.count_words("One two three")
    result3 = processor.count_words("One two three four five")
    assert result1 > result2
    assert result2 < result3
    assert result1 >= 4
    assert result2 <= 3


def test_count_words_empty_string():
    """7. Üres sztring bemenet ellenőrzése"""
    processor = TextProcessor()
    result = processor.count_words("")
    assert result == 0
    assert result is not None


def test_is_palindrome_true_false():
    """8. Assert True/False - boolean ellenőrzés"""
    processor = TextProcessor()
    assert processor.is_palindrome("anna") is True
    assert processor.is_palindrome("indul a pap aludni") is True
    assert processor.is_palindrome("icipici") is True
    assert processor.is_palindrome("a") is True
    assert processor.is_palindrome("hello") is False
    assert processor.is_palindrome("") is False


def test_remove_spaces_multiple_asserts():
    """9. Több assert egy tesztben"""
    processor = TextProcessor()
    result = processor.remove_spaces("a b c d e")
    assert result == "abcde"
    assert " " not in result
    assert len(result) == 5
    assert result.startswith("a")
    assert result.endswith("e")