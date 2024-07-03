from codecs import decode
from Crypto.Cipher import AES
def crack_aes_ecb(ciphertext: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)


if __name__ == "__main__":
    with open("Helper_Functions/7.txt", "r") as file:
        text = file.read()
        text = bytes(text.rstrip(), encoding='utf-8')
        text = decode(text, "base64")

    key = bytes("YELLOW SUBMARINE", encoding='utf-8')
    plaintext = crack_aes_ecb(text, key).decode("ascii")
    print(plaintext)