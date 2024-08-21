import numpy as np

class HillCipher:
    def __init__(self, key_matrix):
        self.key_matrix = np.array(key_matrix)
        self.mod = 26

    def _matrix_mod_inv(self, matrix):
        det = int(np.round(np.linalg.det(matrix)))
        det_inv = pow(det, -1, self.mod)
        matrix_inv = np.round(det_inv * np.linalg.inv(matrix)).astype(int) % self.mod
        return matrix_inv

    def encrypt(self, text):
        text = [ord(c) - ord('A') for c in text.upper() if c.isalpha()]
        padded_text = text + [0] * (len(text) % 2)  # Pad if necessary
        matrix_text = np.array(padded_text).reshape(-1, 2).T
        encrypted_matrix = (self.key_matrix @ matrix_text) % self.mod
        encrypted_text = ''.join([chr(num + ord('A')) for num in encrypted_matrix.flatten()])
        return encrypted_text

    def decrypt(self, text):
        inv_key_matrix = self._matrix_mod_inv(self.key_matrix)
        text = [ord(c) - ord('A') for c in text.upper() if c.isalpha()]
        matrix_text = np.array(text).reshape(-1, 2).T
        decrypted_matrix = (inv_key_matrix @ matrix_text) % self.mod
        decrypted_text = ''.join([chr(num + ord('A')) for num in decrypted_matrix.flatten()])
        return decrypted_text
