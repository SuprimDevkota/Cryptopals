from itertools import combinations
from codecs import decode
from Q3_Single_byte_XOR_Cipher import crack_xor_cipher
from Q5_Implement_Repeating_key_XOR import repeating_key_xor

def hamming_distance_calculator(b1: bytes, b2: bytes) -> int:
    if not isinstance(b1, bytes) or not isinstance(b2, bytes):
        raise ValueError("Inputs are not bytes.")
    
    if len(b1) != len(b2):
        raise ValueError("Bytes are of different length")
    
    dist = 0
    for byte1, byte2 in zip(b1, b2):
        dist += bin(byte1 ^ byte2).count('1')

    return dist


def find_key_length(text: bytes) -> int:    
    # lower is better
    min_score = float('inf')

    for KEYSIZE in range(2, 40):
        chunks = [text[start:start + KEYSIZE] for start in range(0, len(text), KEYSIZE)]
        subgroup = chunks[:4]
        average_score = (sum(hamming_distance_calculator(a, b) for a,b in combinations(subgroup, 2)) / 6) / KEYSIZE
        
        if average_score < min_score:
            min_score = average_score
            key_length = KEYSIZE

    return key_length

def chunker(ciphertext: bytes) -> tuple[list, int]:
    chunk_length = find_key_length(ciphertext)
    block_list = [ciphertext[i:i + chunk_length] for i in range(0, len(ciphertext), chunk_length)]
    return block_list, chunk_length

def transposer(block_list: list, chunk_length: int) -> list:
    transposed_list = []
    for i in range(chunk_length):
        conc_bytes = b''
        for byte in block_list:
            if i < len(byte):
                conc_bytes += byte[i:i+1]
        transposed_list.append(conc_bytes)
    return transposed_list

def crack_repeating_xor_key(ciphertext: bytes) -> bytes:
    block_list, chunk_length = chunker(ciphertext)
    transposed_list = transposer(block_list, chunk_length)
    key = ""
    for bytestring in transposed_list:
        key += crack_xor_cipher(bytestring)[2]
    return key


if __name__ == "__main__":
    with open("../Helper_Functions/6.txt", "r") as file:
        text = file.read()
        text = bytes(text.rstrip(), encoding='utf-8')
        text = decode(text, "base64")
    
    key = crack_repeating_xor_key(text)
    print(repeating_key_xor(text, key).decode("ascii"))
    