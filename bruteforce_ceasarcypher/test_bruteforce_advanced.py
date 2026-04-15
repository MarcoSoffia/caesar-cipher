#!/usr/bin/env python3

import pytest

try:
    from caesar_breaker import brute_force
except ImportError:
    brute_force = None

def test_brute_force_empty_string():
    """Check behavior with empty string"""
    try:
        result = brute_force("")
        assert len(result) == 26, "Should return 26 results even for empty string"
        for key, text in result:
            assert text == "", f"Empty input should give empty output for all keys"
    except Exception as e:
        pytest.fail(f"Crashed with empty string: {e}")

def test_brute_force_preserves_non_letters():
    """Check that numbers, spaces, and punctuation are preserved"""
    ciphertext = "Abc 123! Xyz."
    result = brute_force(ciphertext)

    for key, text in result:
        # Count non-letter characters
        original_non_letters = sum(1 for c in ciphertext if not c.isalpha())
        result_non_letters = sum(1 for c in text if not c.isalpha())

        assert original_non_letters == result_non_letters, (
            f"Non-letters not preserved with key {key}: "
            f"expected {original_non_letters}, got {result_non_letters}"
        )

def test_brute_force_preserves_case():
    """Check that uppercase/lowercase is preserved"""
    ciphertext = "AbC"
    result = brute_force(ciphertext)

    for key, text in result:
        assert len(text) == 3, f"Length should be 3, got {len(text)}"
        assert text[0].isupper(), f"First char should be uppercase with key {key}"
        assert text[1].islower(), f"Second char should be lowercase with key {key}"
        assert text[2].isupper(), f"Third char should be uppercase with key {key}"

def test_brute_force_all_keys_unique():
    """Check that all 26 keys produce different results (for alphabetic input)"""
    ciphertext = "AAAA"
    result = brute_force(ciphertext)

    texts = [text for key, text in result]
    unique_texts = set(texts)

    assert len(unique_texts) == 26, (
        f"Expected 26 unique results, got {len(unique_texts)}. "
        "All keys should produce different outputs for alphabetic input."
    )

def test_brute_force_keys_in_order():
    """Check that keys are returned in order from 0 to 25"""
    result = brute_force("TEST")

    for i, (key, text) in enumerate(result):
        assert key == i, f"Expected key {i} at position {i}, got key {key}"

def test_brute_force_complex_message():
    """Test with a realistic message"""
    # "The quick brown fox jumps!" encrypted with key 7
    ciphertext = "Aol xbpjr iyvdu mve qbtwz!"
    result = brute_force(ciphertext)

    # Key 19 should decrypt it (26 - 7 = 19)
    decrypted = next((text for key, text in result if key == 19), None)
    assert decrypted.lower() == "the quick brown fox jumps!", (
        f"Failed to decrypt complex message. Got: {decrypted}"
    )