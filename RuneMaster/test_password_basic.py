#!/usr/bin/env python3
"""
test_password_basic.py
Test base per l'esercizio password generator.
Verifica: esistenza funzione, lunghezza, composizione default, singoli set.
"""

import string
import pytest

try:
    from password_generator import generate_password
except ImportError:
    generate_password = None


def test_structure_check():
    """Verify that password_generator.py exists and exposes generate_password"""
    assert generate_password is not None, (
        "CRITICAL ERROR: Could not find 'generate_password' in 'password_generator.py'. "
        "Make sure your file is named exactly 'password_generator.py' "
        "and your function is named 'generate_password'."
    )


def test_default_length():
    """Default call produces a 12-character password"""
    pwd = generate_password()
    assert isinstance(pwd, str), f"Expected str, got {type(pwd)}"
    assert len(pwd) == 12, f"Expected length 12, got {len(pwd)}"


def test_custom_length():
    """Length parameter is honoured"""
    for n in (8, 16, 24, 64):
        pwd = generate_password(length=n)
        assert len(pwd) == n, f"Expected length {n}, got {len(pwd)}"


def test_default_contains_all_sets():
    """Default password contains at least one char from each of the 4 sets"""
    pwd = generate_password(length=20)
    assert any(c in string.ascii_uppercase for c in pwd), (
        f"Expected at least one uppercase letter, got: {pwd!r}"
    )
    assert any(c in string.ascii_lowercase for c in pwd), (
        f"Expected at least one lowercase letter, got: {pwd!r}"
    )
    assert any(c in string.digits for c in pwd), (
        f"Expected at least one digit, got: {pwd!r}"
    )
    assert any(c in string.punctuation for c in pwd), (
        f"Expected at least one symbol, got: {pwd!r}"
    )


def test_only_digits():
    """Disabling all sets except digits yields a numeric-only password"""
    pwd = generate_password(
        length=16,
        use_upper=False,
        use_lower=False,
        use_digits=True,
        use_symbols=False,
    )
    assert all(c in string.digits for c in pwd), (
        f"Expected only digits, got: {pwd!r}"
    )


def test_only_lowercase():
    """Disabling all sets except lowercase yields an alpha-lower password"""
    pwd = generate_password(
        length=16,
        use_upper=False,
        use_lower=True,
        use_digits=False,
        use_symbols=False,
    )
    assert all(c in string.ascii_lowercase for c in pwd), (
        f"Expected only lowercase letters, got: {pwd!r}"
    )


def test_two_calls_produce_different_passwords():
    """A CSPRNG should never produce the same 20-char password twice in a row"""
    pwd1 = generate_password(length=20)
    pwd2 = generate_password(length=20)
    assert pwd1 != pwd2, (
        "Two consecutive calls returned identical passwords — "
        "is the generator actually random?"
    )
