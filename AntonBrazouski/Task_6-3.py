class Cipher:

    def __init__(self, keyword='CRYPTO'):     
        self.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ' # noncapital?
        self.cipher = self.generate_cipher('CRYPTO')

    def encode(self, astring):
        code = ''
        for letter in astring:
            pos = self.letters.index(letter)
            code += self.cipher[pos]

        return code

    def generate_cipher(self, keyword='CRYPTO'):
        letters_clean = ''
        for ch in self.letters:
            if ch not in keyword:
                letters_clean += ch
        result = keyword + letters_clean

        return result

               


cipher = Cipher("CRYPTO")
print(cipher.encode("HELLOW ORLD"))