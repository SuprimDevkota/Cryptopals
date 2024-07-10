from codecs import encode, decode
from Crypto.Cipher import AES
from typing import Union

def chunker(ciphertext: bytes, chunk_length:int) -> list[bytes]:
    return [ciphertext[start:start+chunk_length] for start in range(0, len(ciphertext), chunk_length)]


def pad_bytestring_multiple(plaintext: bytes, multiple_of: int) -> bytes:

    required_length = len(plaintext)
    while required_length % multiple_of != 0:
        required_length += 1
    
    padding_length = required_length - len(plaintext)
    padding_character = bytes([int(str(padding_length), 16)])
    while padding_length > 0:
        plaintext += padding_character
        padding_length -= 1
    return plaintext

def encrypt_aes_ecb(plaintext: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad_bytestring_multiple(plaintext, 16)
    ciphertext = cipher.encrypt(padded_data)
    return ciphertext

def decrypt_aes_ecb(ciphertext: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad_bytestring_multiple(ciphertext, 16)
    plaintext = cipher.decrypt(padded_data)
    return plaintext

def encrypt_aes_cbc(plaintext: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CBC)
    padded_data = pad_bytestring_multiple(plaintext, 16)
    ciphertext = cipher.encrypt(padded_data)
    return ciphertext

def detect_aes_ecb(ciphertext: bytes) -> bool:
    chunked_bytestrings = chunker(ciphertext, AES.block_size)
    num_chunked_bytestrings = len(chunked_bytestrings)
    num_unique_chunked_bytestrings = len(set(chunked_bytestrings))
    num_repeated_chunked_bytestrings = num_chunked_bytestrings - num_unique_chunked_bytestrings

    if num_repeated_chunked_bytestrings > 0:
        return True
    return False

def fixed_xor(f: bytes, s: Union[int, bytes]) -> bytes:
    # If s is a single integer then xor that integer with every bit of the byte string.
    if type(s) == int:
        r = bytes([s ^ fb for fb in f])
        
    # If both are byte strings. First check if they have same length and then xor them bit by bit.
    elif type(f) == type(s) == bytes:
        if len(f) != len(s):
            print("Byte strings are of different length")
            return 1
        r = bytes([fb^ sb for fb, sb in zip(f, s)])

    return r