"""
Takes two byte-strings as input. XORs them bit by bit and outputs the result as a byte
"""
def fixed_xor(f: bytes, s: bytes) -> bytes:
    if len(f) != len(s):
        print("Byte strings are of different length")
        return 1
    r = ''.join([chr(fb^ sb) for fb, sb in zip(f, s)]).encode()
    return r

if __name__ == "__main__":
    first_string = "1c0111001f010100061a024b53535009181c"
    second_string = "686974207468652062756c6c277320657965"

    print(fixed_xor(bytes.fromhex(first_string), bytes.fromhex(second_string)).hex())

