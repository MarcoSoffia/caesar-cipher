#!/usr/bin/env python3

import pytest

# We try to import the function here to check if the file/function exists
try:
    from caesar_cipher import encrypt
except ImportError:
    encrypt = None
    
def test_structure_check():
    """Verify that the file and function are named correctly"""
    assert encrypt is not None, (
        "CRITICAL ERROR: Could not find 'encrypt' in 'caesar_cipher.py'. "
        "Make sure your file is named exactly 'caesar_cipher.py' "
        "and your function is named 'encrypt'."
    )
    
def test_basic_translation():
    """Check a simple shift with key 3 (Standard Caesar)"""
    result = encrypt("abc", 3)
    assert result == "def", f"Expected 'def', but your function returned '{result}'"
    
def test_case_preservation():
    """Check if uppercase letters stay uppercase"""
    result = encrypt("ABC", 3)
    assert result == "DEF", f"Uppercase letters should remain uppercase. Expected 'DEF', got '{result}'"
    
def test_space_preservation():
    """Check if spaces remain untouched"""
    result = encrypt("a b c", 1)
    assert result == "b c d", f"Spaces should not be modified. Got: '{result}'"
    
def test_alphabet_wrap():
    """Check if 'z' wraps back to 'a'"""
    result = encrypt("xyz", 2)
    assert result == "zab", f"The alphabet should wrap around (z -> a). Expected 'zab', got '{result}'"