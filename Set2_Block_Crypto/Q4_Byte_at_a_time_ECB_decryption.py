import sys
sys.path.append("../")
from utils.my_utils import AES, detect_aes_ecb, decode, key_gen, encrypt_aes_ecb

RANDOM_KEY = key_gen(16)

def ecb_encryption_oracle(plaintext: bytes) -> bytes:
    unknown_bytestring = b"Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg\naGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq\ndXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg\nYnkK"
    to_append = decode(unknown_bytestring, "base64")
    appended_plaintext = plaintext + to_append
    return encrypt_aes_ecb(appended_plaintext, RANDOM_KEY) 


def find_block_size() -> int:
    prev_first_byte = bytes(0)
    for i in range(2, 50):
        plain_text = b"A" * i
        cipher_text = ecb_encryption_oracle(plain_text)
        current_first_byte = cipher_text[0]

        if prev_first_byte == current_first_byte:
            return i-1
        
        prev_first_byte = current_first_byte
    
    exit("Block size not found!")


def detect_aes_ecb_unknown_ct() -> bool:
    for i in range(2, 50):
        plaintext = b"A" * i
        cipher_text = ecb_encryption_oracle(plaintext)
        if detect_aes_ecb(cipher_text) == True:
            return True
    return False


def find_payload_length() -> int:
    previous_length = len(ecb_encryption_oracle(b''))
    for i in range(10):
        length  = len(ecb_encryption_oracle(b'A' * i))
        if length != previous_length:
            return previous_length - i


def crack_aes_ecb_byte_at_a_time(known_pt: bytes) -> bytes:

    known_pt_length = len(known_pt)
    padding_size = (-known_pt_length - 1) % AES.block_size
    crafted_input_block = b"A" * padding_size
    target_block_number = known_pt_length // AES.block_size
    target_slice = slice(target_block_number* AES.block_size, (target_block_number + 1) * AES.block_size)
    required_cipher_block = ecb_encryption_oracle(crafted_input_block)[target_slice]

    for candidate_byte in range(255):
        candidate_input_block = b"A" * padding_size + known_pt + bytes([candidate_byte])

        candidate_cipher_block = ecb_encryption_oracle(candidate_input_block)[target_slice]

        if required_cipher_block == candidate_cipher_block:
            return bytes([candidate_byte])
    
    return -1


def crack_aes_ecb() -> bytes:
    block_size = find_block_size()
    if detect_aes_ecb_unknown_ct() == True:
        print(f"{block_size=}")
        plaintext = b""
        for _ in range(find_payload_length()):
            plaintext += crack_aes_ecb_byte_at_a_time(plaintext)
        return plaintext
    
    else:
        exit("AES ECB is not used.")

if __name__ == "__main__":
    result = crack_aes_ecb()
    print(result.decode("ascii"))
