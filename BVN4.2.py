def encrypt_substitution(plaintext, k):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + k) % 26 + shift)
        else:
            result += char
    return result

P = "HoangThiThuThuy"
k = 14
C = encrypt_substitution(P, k)

print("Plaintext :", P)
print("Ciphertext:", C)
