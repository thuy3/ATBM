def rsa_encrypt(plaintext, e, n):
    ciphertext = []
    for char in plaintext.upper():
        if char.isalpha():
            P = ord(char) - 65  # đổi sang số 0-25
            C = pow(P, e, n)   # (P^e) mod n
            ciphertext.append(C)
        else:
            ciphertext.append(char)
    return ciphertext

# Thông số
p, q, e = 17, 23, 5
n = p * q  # 391
plaintext = "HoangThiThuThuy"

# Mã hoá
cipher = rsa_encrypt(plaintext, e, n)

print("Plaintext :", plaintext)
print("Ciphertext:", cipher)
