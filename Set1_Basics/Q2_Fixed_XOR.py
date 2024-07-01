"""
Takes two byte-strings as input. XORs them bit by bit and outputs the result as a byte.
Optionally if it gets a single int as second input in place of byte it XORs that with all bits in the first bytestring.
"""
def fixed_xor(f: bytes, s: tuple[int, bytes]) -> bytes:
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

if __name__ == "__main__":
    first_string = "1c0111001f010100061a024b53535009181c"
    second_string = "686974207468652062756c6c277320657965"

    print(fixed_xor(bytes.fromhex(first_string), bytes.fromhex(second_string)).hex())

