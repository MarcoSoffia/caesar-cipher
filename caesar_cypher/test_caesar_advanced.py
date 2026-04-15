#!/usr/bin/env python3

import pytest

try:
    from caesar_cipher import encrypt
except ImportError:
    encrypt = None
    
def test_huge_keys():
    """Check keys much larger than 26 (using modulo)"""
    # 27 is 26 (full circle) + 1
    result = encrypt("abc", 27)
    assert result == "bcd", f"A key of 27 should behave like a key of 1. Expected 'bcd', got '{result}'"
    
    result_static = encrypt("abc", 5200)
    assert result_static == "abc", "A key that is a multiple of 26 should not change the text."
    
def test_extreme_negative_keys():
    """Check negative keys beyond -26"""
    # -27 is effectively -1
    result = encrypt("bcd", -27)
    assert result == "abc", f"A key of -27 should behave like -1. Expected 'abc', got '{result}'"
    
def test_non_alphabetic_characters():
    """Check that numbers, punctuation, and emojis are ignored"""
    input_text = "Hello 123! 😊"
    result = encrypt(input_text, 1)
    # Only 'H', 'e', 'l', 'l', 'o' should change
    expected = "Ifmmp 123! 😊"
    assert result == expected, f"Symbols, numbers, and emojis should not change. Expected '{expected}', got '{result}'"
    
def test_empty_string():
    """Check if the function handles empty input without crashing"""
    try:
        result = encrypt("", 10)
        assert result == "", "An empty string input should return an empty string."
    except Exception as e:
        pytest.fail(f"Your function crashed when receiving an empty string. Error: {e}")
        
def test_round_trip():
    """Check if encrypting and then decrypting returns the original text"""
    original = "Zebra 2026! Does it work?"
    key = 15
    encrypted = encrypt(original, key)
    decrypted = encrypt(encrypted, -key)
    assert decrypted == original, "Encrypting and then decrypting with the same key must return the original text."