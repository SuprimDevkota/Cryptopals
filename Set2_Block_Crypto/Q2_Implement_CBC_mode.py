import sys
sys.path.append("../")
from utils.my_utils import AES, decode, chunker, decrypt_aes, fixed_xor

def decrypt_cbc(cipher_text: bytes, key: bytes, block_size: int, iv: 0) -> bytes:
    
    chunked_bytestrings = chunker(cipher_text, block_size)
    plaintext = b''

    for bytestring in chunked_bytestrings:
        decrypted_ct = decrypt_aes(bytestring, key)
        plaintext += fixed_xor(decrypted_ct, iv)
        iv = bytestring

    return plaintext

if __name__ == "__main__":    
    with open("../Files/10.txt", "r") as file:
        text = file.read()
        text = bytes(text, encoding='utf-8')
        text = decode(text, encoding="base64")

    key = b"YELLOW SUBMARINE"
    BLOCK_SIZE = AES.block_size
    IV = 0
    plaintext = b""

    print(decrypt_cbc(text, key, BLOCK_SIZE, IV).decode("ascii"))


