from Q2_Fixed_XOR import fixed_xor

expected_frequencies = {
 'a': 0.07570509197644527,
 'b': 0.01506809356256039,
 'c': 0.02196860585951031,
 'd': 0.039352062861205815,
 'e': 0.12440976463510237,
 'f': 0.019315965069005122,
 'g': 0.018158283349437566,
 'h': 0.06452936136077737,
 'i': 0.06135713113708045,
 'j': 0.0014676122586643817,
 'k': 0.008796557947895207,
 'l': 0.04496727498131301,
 'm': 0.028805308927822647,
 'n': 0.0644108585075933,
 'o': 0.08501212375344114,
 'p': 0.014603197753915153,
 'q': 0.0006654390986490675,
 'r': 0.062241344733915516,
 's': 0.06252392846073909,
 't': 0.09279684964722612,
 'u': 0.03432024940292793,
 'v': 0.010036280104282511,
 'w': 0.022132686733149807,
 'x': 0.0014220342382089662,
 'y': 0.02565130991230789,
 'z': 0.00027346812273249346
}

def score_text(text: bytes) -> float:
    score = 0.0
    l = len(text)
    for letter, expected_frequency in expected_frequencies.items():
        actual_frequency = text.count(ord(letter)) / l
        err = abs(actual_frequency - expected_frequency)
        score += err
    return score

def crack_xor_cipher(ciphertext: bytes) -> tuple[bytes, int]:
    best_guess = (float('inf'), None, '')

    for candidate_key in range(256):
        plaintext = fixed_xor(ciphertext, candidate_key)
        score = score_text(plaintext)
        curr_guess = (score, plaintext, chr(candidate_key))
        best_guess = min(best_guess, curr_guess)
    
    return (best_guess[1], best_guess[2])

if __name__ == "__main__":
    hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    byte_string = bytes.fromhex(hex_string)
    result = crack_xor_cipher(byte_string)
    print(result)