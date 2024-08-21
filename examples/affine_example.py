from affine_cipher import AffineCipher

cipher = AffineCipher(5, 8)
encrypted = cipher.encrypt("HELLO WORLD")
decrypted = cipher.decrypt(encrypted)

print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
