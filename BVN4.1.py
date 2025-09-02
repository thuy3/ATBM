def encrypt_caesar(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():  
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char  
    return result

plaintext = "Hoang Thi Thu Thuy"  
key = 14
ciphertext = encrypt_caesar(plaintext, key)

print("Plaintext :", plaintext)
print("Ciphertext:", ciphertext)
