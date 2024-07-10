import secrets
import sys
sys.path.append("../") #Current working directory should be inside Set2_Block_Crypto folder

from utils.my_utils import encrypt_aes_ecb, encrypt_aes_cbc, detect_aes_ecb
def key_gen(key_length: int) -> bytes:
    key = secrets.token_bytes(key_length)
    return key

def encryption_oracle(plaintext: bytes) -> bytes:
    random_key = key_gen(16)
    before_append_length = secrets.choice(range(5,10))
    after_append_length = secrets.choice(range(5,10))
    appended_plaintext = key_gen(before_append_length) + plaintext + key_gen(after_append_length)

    choice = secrets.choice([0,1])
    if choice == 0:
        return encrypt_aes_ecb(appended_plaintext, random_key)
    else:
        return encrypt_aes_cbc(appended_plaintext, random_key)
    

if __name__ == "__main__":
    plaintext = b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    ciphertext = encryption_oracle(plaintext)
    if detect_aes_ecb(ciphertext) == True:
        print("ECB was used")
    else:
        print("CBC was used")