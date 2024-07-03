def repeating_key_xor(ciphertext: bytes, key: str) -> bytes:
    key_list = [ord(x) for x in key]
    count = -1
    result = b''
    for byte in ciphertext:
        count = (count + 1) % len(key_list)
        result += bytes([byte ^ key_list[count]])
    return result

if __name__ == "__main__":
    string = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    
    byte_string = bytes(string, encoding='utf-8')
    key = "ICE"
    plaintext = repeating_key_xor(byte_string, key)
    print(plaintext.hex())