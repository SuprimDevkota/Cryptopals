from Crypto.Cipher import AES

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