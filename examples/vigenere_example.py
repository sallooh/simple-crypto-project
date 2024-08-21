from vigenere_cipher import VigenereCipher

cipher = VigenereCipher("KEY")
encrypted = cipher.encrypt("HELLO WORLD")
decrypted = cipher.decrypt(encrypted)

print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
