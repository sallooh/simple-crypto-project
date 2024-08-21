class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()
        self.mod = 26

    def _shift_char(self, char, shift):
        return chr((ord(char) - ord('A') + shift) % self.mod + ord('A'))

    def encrypt(self, text):
        text = text.upper()
        key = self.key
        return ''.join([self._shift_char(text[i], ord(key[i % len(key)]) - ord('A')) if char.isalpha() else char for i, char in enumerate(text)])

    def decrypt(self, text):
        text = text.upper()
        key = self.key
        return ''.join([self._shift_char(text[i], -(ord(key[i % len(key)]) - ord('A'))) if char.isalpha() else char for i, char in enumerate(text)])
