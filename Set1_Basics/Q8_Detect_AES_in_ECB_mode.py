def chunker(ciphertext: bytes, chunk_length:int) -> list[bytes]:
    return [ciphertext[start:start+chunk_length] for start in range(0, len(ciphertext), chunk_length)]

def detect_aes_ecb(lines: list, chunk_length: int) -> int:
    for i, line in enumerate(lines):
        chunked_bytestrings = chunker(line, chunk_length)
        num_chunked_bytestrings = len(chunked_bytestrings)
        num_unique_chunked_bytestrings = len(set(chunked_bytestrings))
        num_repeated_chunked_bytestrings = num_chunked_bytestrings - num_unique_chunked_bytestrings

        if num_repeated_chunked_bytestrings > 0:
            return i
    return -1

if __name__ == "__main__":
    with open ("Helper_Functions/8.txt", "r") as file:
        lines = file.readlines()
        lines = [bytes.fromhex(line.rstrip()) for line in lines]
    
    chunk_size = 16

    index = detect_aes_ecb(lines, chunk_size)
    print(f"The bytestring using AES in ECB Mode is at index {index} and is {lines[index]}")
