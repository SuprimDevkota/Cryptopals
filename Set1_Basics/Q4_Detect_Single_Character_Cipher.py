from Q3_Single_byte_XOR_Cipher import crack_xor_cipher

if __name__ == "__main__":
    with open("../Helper_Functions/file.txt", "r") as file:
        lines = file.readlines()
        lines = [bytes.fromhex(line.rstrip()) for line in lines]

    best_guess = (float('inf'), None)
    for line in lines:
        curr_guess = crack_xor_cipher(line)
        best_guess = min(curr_guess, best_guess)

    print(best_guess)