#!/usr/bin/env python3
"""
test_password_advanced.py
Test avanzati per l'esercizio password generator.
Verifica: vincolo almeno-un-char-per-set, errori, caratteri ambigui, statistica.
"""

import string
import pytest

try:
    from password_generator import generate_password
except ImportError:
    generate_password = None


AMBIGUOUS = set("Il1O0")


def test_structure_check():
    """Verify that password_generator.py exists and exposes generate_password"""
    assert generate_password is not None, (
        "CRITICAL ERROR: Could not find 'generate_password' in 'password_generator.py'."
    )


def test_all_sets_disabled_raises():
    """Disabling every set must raise ValueError, not return an empty string"""
    with pytest.raises(ValueError):
        generate_password(
            length=12,
            use_upper=False,
            use_lower=False,
            use_digits=False,
            use_symbols=False,
        )


def test_length_smaller_than_enabled_sets_raises():
    """length=2 with 4 enabled sets cannot satisfy the one-per-set guarantee"""
    with pytest.raises(ValueError):
        generate_password(
            length=2,
            use_upper=True,
            use_lower=True,
            use_digits=True,
            use_symbols=True,
        )


def test_minimum_length_equals_enabled_sets():
    """length==number_of_enabled_sets must work and contain one char per set"""
    pwd = generate_password(
        length=4,
        use_upper=True,
        use_lower=True,
        use_digits=True,
        use_symbols=True,
    )
    assert len(pwd) == 4
    assert any(c in string.ascii_uppercase for c in pwd)
    assert any(c in string.ascii_lowercase for c in pwd)
    assert any(c in string.digits for c in pwd)
    assert any(c in string.punctuation for c in pwd)


def test_one_char_per_set_guarantee_repeated():
    """Over many runs, short passwords must always contain one char per enabled set"""
    for _ in range(200):
        pwd = generate_password(
            length=4,
            use_upper=True,
            use_lower=True,
            use_digits=True,
            use_symbols=True,
        )
        assert any(c in string.ascii_uppercase for c in pwd), pwd
        assert any(c in string.ascii_lowercase for c in pwd), pwd
        assert any(c in string.digits for c in pwd), pwd
        assert any(c in string.punctuation for c in pwd), pwd


def test_avoid_ambiguous_removes_confusing_chars():
    """With avoid_ambiguous=True, I, l, 1, O, 0 must never appear"""
    for _ in range(50):
        pwd = generate_password(length=64, avoid_ambiguous=True)
        offenders = [c for c in pwd if c in AMBIGUOUS]
        assert not offenders, (
            f"Found ambiguous chars {offenders} in password {pwd!r}"
        )


def test_disabled_set_never_appears():
    """A disabled set must never contribute characters, not even occasionally"""
    for _ in range(50):
        pwd = generate_password(length=40, use_symbols=False)
        offenders = [c for c in pwd if c in string.punctuation]
        assert not offenders, (
            f"Found symbols {offenders} in a no-symbol password: {pwd!r}"
        )


def test_distribution_is_not_trivially_biased():
    """Over a large sample the first character is not always the same"""
    first_chars = {generate_password(length=20)[0] for _ in range(100)}
    assert len(first_chars) > 10, (
        f"First char has only {len(first_chars)} distinct values over 100 runs — "
        "the generator looks biased or not random at all."
    )
