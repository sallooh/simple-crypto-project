from hill_cipher import HillCipher

key_matrix = [[6, 24], [1, 16]]
cipher = HillCipher(key_matrix)
encrypted = cipher.encrypt("HELLO")
decrypted = cipher.decrypt(encrypted)

print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
