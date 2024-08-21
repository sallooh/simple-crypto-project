class AffineCipher:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.mod = 26

    def encrypt(self, text):
        return ''.join([chr((self.a * (ord(char) - ord('A')) + self.b) % self.mod + ord('A')) if char.isalpha() else char for char in text.upper()])

    def decrypt(self, text):
        a_inv = pow(self.a, -1, self.mod)
        return ''.join([chr((a_inv * (ord(char) - ord('A') - self.b)) % self.mod + ord('A')) if char.isalpha() else char for char in text.upper()])
