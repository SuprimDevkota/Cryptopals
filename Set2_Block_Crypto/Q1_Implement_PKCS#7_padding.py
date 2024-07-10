def pad_bytestring(plaintext: bytes, required_length: int) -> bytes:
    padding_length = required_length - len(plaintext)
    padding_character = bytes([int(str(padding_length), 16)])
    while padding_length > 0:
        plaintext += padding_character
        padding_length -= 1
    return plaintext

if __name__ == "__main__":
    plaintext = "YELLOW SUBMARINE"
    bytestring = bytes(plaintext, encoding='utf-8')
    required_length = 20
    print(pad_bytestring(bytestring, required_length))