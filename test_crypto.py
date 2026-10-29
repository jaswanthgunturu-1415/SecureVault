
import pytest

from crypto_utils import (
    encrypt_file,
    decrypt_file,
    calculate_sha256,
    verify_integrity,
)


def test_encrypt_and_decrypt():
    original = b"My confidential file"
    encrypted = encrypt_file(original, "StrongPassword123!")
    assert decrypt_file(encrypted, "StrongPassword123!") == original


def test_wrong_password_fails():
    encrypted = encrypt_file(b"Secret data", "StrongPassword123!")
    with pytest.raises(ValueError):
        decrypt_file(encrypted, "WrongPassword123!")


def test_modified_data_fails():
    encrypted = bytearray(
        encrypt_file(b"Secret data", "StrongPassword123!")
    )
    encrypted[-1] ^= 1

    with pytest.raises(ValueError):
        decrypt_file(bytes(encrypted), "StrongPassword123!")


def test_empty_file():
    encrypted = encrypt_file(b"", "StrongPassword123!")
    assert decrypt_file(encrypted, "StrongPassword123!") == b""


def test_each_encryption_is_different():
    first = encrypt_file(b"Same content", "StrongPassword123!")
    second = encrypt_file(b"Same content", "StrongPassword123!")

    assert first != second
    assert decrypt_file(first, "StrongPassword123!") == b"Same content"
    assert decrypt_file(second, "StrongPassword123!") == b"Same content"


def test_sha256_is_consistent():
    data = b"Secure file encryption project"
    assert calculate_sha256(data) == calculate_sha256(data)


def test_integrity_passes_for_matching_files():
    assert verify_integrity(b"Original", b"Original") is True


def test_integrity_fails_for_different_files():
    assert verify_integrity(b"Original", b"Modified") is False
