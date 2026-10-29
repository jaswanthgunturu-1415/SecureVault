
import os
import hashlib

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

MAGIC = b"SFE1"
SALT_SIZE = 16
NONCE_SIZE = 12
KEY_SIZE = 32


def derive_key(password: str, salt: bytes) -> bytes:
    """Derive a 256-bit encryption key from a password."""
    if not password:
        raise ValueError("Password cannot be empty.")

    kdf = Scrypt(
        salt=salt,
        length=KEY_SIZE,
        n=2**14,
        r=8,
        p=1,
    )
    return kdf.derive(password.encode("utf-8"))


def encrypt_file(data: bytes, password: str) -> bytes:
    """Encrypt file bytes using AES-256-GCM."""
    salt = os.urandom(SALT_SIZE)
    nonce = os.urandom(NONCE_SIZE)

    key = derive_key(password, salt)
    ciphertext = AESGCM(key).encrypt(nonce, data, MAGIC)

    return MAGIC + salt + nonce + ciphertext


def decrypt_file(package: bytes, password: str) -> bytes:
    """Decrypt an encrypted package and authenticate its contents."""
    header_size = len(MAGIC) + SALT_SIZE + NONCE_SIZE

    if len(package) < header_size + 16:
        raise ValueError("Invalid or incomplete encrypted file.")

    if not package.startswith(MAGIC):
        raise ValueError("This is not a supported encrypted file.")

    salt_start = len(MAGIC)
    nonce_start = salt_start + SALT_SIZE
    data_start = nonce_start + NONCE_SIZE

    salt = package[salt_start:nonce_start]
    nonce = package[nonce_start:data_start]
    ciphertext = package[data_start:]

    key = derive_key(password, salt)

    try:
        return AESGCM(key).decrypt(nonce, ciphertext, MAGIC)
    except InvalidTag:
        raise ValueError(
            "Decryption failed. The password may be wrong, "
            "or the encrypted file may have been modified."
        ) from None


def calculate_sha256(data: bytes) -> str:
    """Return the SHA-256 hexadecimal digest of file contents."""
    return hashlib.sha256(data).hexdigest()


def verify_integrity(original: bytes, recovered: bytes) -> bool:
    """Compare SHA-256 fingerprints of two files."""
    return calculate_sha256(original) == calculate_sha256(recovered)
