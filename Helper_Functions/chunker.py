def chunker(ciphertext: bytes, chunk_length:int) -> list[bytes]:
    return [ciphertext[start:start+chunk_length] for start in range(0, len(ciphertext), chunk_length)]