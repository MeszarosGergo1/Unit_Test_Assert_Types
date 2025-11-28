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


def test_reverse_text_not_in():
    """4. Assert not in - nincs benne"""
    processor = TextProcessor()
    result = processor.reverse_text("hello")
    assert "hello" not in result


def test_count_words_isinstance():
    """5. Assert isinstance - típus ellenőrzés"""
    pass


def test_count_words_greater_less():
    """6. Assert >, <, >=, <= - összehasonlítás"""
    pass


def test_count_words_empty_string():
    """7. Üres sztring bemenet ellenőrzése"""
    pass


def test_is_palindrome_true_false():
    """8. Assert True/False - boolean ellenőrzés"""
    pass


def test_remove_spaces_multiple_asserts():
    """9. Több assert egy tesztben"""
    pass