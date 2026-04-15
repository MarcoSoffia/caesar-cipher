#!/usr/bin/env python3

import pytest

# Import verificato con try/except
try:
    from caesar_breaker import brute_force
except ImportError:
    brute_force = None

def test_structure_check():
    """Verify that the file and function are named correctly"""
    assert brute_force is not None, (
        "CRITICAL ERROR: Could not find 'brute_force' in 'caesar_breaker.py'. "
        "Make sure your file is named exactly 'caesar_breaker.py' "
        "and your function is named 'brute_force'."
    )

def test_brute_force_returns_list():
    """Check that brute_force returns a list"""
    result = brute_force("TEST")
    assert isinstance(result, list), "brute_force should return a list"

def test_brute_force_returns_26_results():
    """Check that brute_force tries all 26 keys"""
    result = brute_force("HELLO")
    assert len(result) == 26, f"Expected 26 results, got {len(result)}"

def test_brute_force_returns_tuples():
    """Check that each result is a tuple (key, text)"""
    result = brute_force("ABC")
    for item in result:
        assert isinstance(item, tuple), f"Each result should be a tuple, got {type(item)}"
        assert len(item) == 2, f"Each tuple should have 2 elements, got {len(item)}"
        assert isinstance(item[0], int), f"First element should be int (key), got {type(item[0])}"
        assert isinstance(item[1], str), f"Second element should be str (text), got {type(item[1])}"

def test_brute_force_includes_key_zero():
    """Check that key 0 (no shift) is included"""
    original = "Hello, World!"
    result = brute_force(original)

    # Key 0 should return the original text
    key_zero_result = next((text for key, text in result if key == 0), None)
    assert key_zero_result == original, "Key 0 should return the original text unchanged"

def test_brute_force_finds_correct_key():
    """Check that brute force can find the original message"""
    # We know "Khoor" is "Hello" with key 3
    ciphertext = "Khoor"
    result = brute_force(ciphertext)

    # Find result with key 23 (which is -3 mod 26, the decryption key)
    decrypted = next((text for key, text in result if key == 23), None)
    assert decrypted == "Hello", f"Expected 'Hello' with key 23, got '{decrypted}'"