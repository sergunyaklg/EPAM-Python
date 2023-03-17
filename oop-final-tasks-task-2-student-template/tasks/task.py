class Cipher:
    def __init__(self, keyword):
        self.keyword = keyword
        self.key = self.generate_key()

    def generate_key(self):
        # Remove repeated characters from keyword and add to front of alphabet
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        key = "".join(dict.fromkeys(self.keyword.upper()))
        key_alphabet = key + "".join([c for c in alphabet if c not in key])
        return key_alphabet

    def encode(self, message):
        encoded_message = ""
        for char in message:
            if char.isalpha():
                index = ord(char.upper()) - ord('A')
                encoded_char = self.key[index]
                if char.islower():
                    encoded_char = encoded_char.lower()
                encoded_message += encoded_char
            else:
                encoded_message += char
        return encoded_message

    def decode(self, message):
        decoded_message = ""
        for char in message:
            if char.isalpha():
                index = self.key.index(char.upper())
                decoded_char = chr(index + ord('A'))
                if char.islower():
                    decoded_char = decoded_char.lower()
                decoded_message += decoded_char
            else:
                decoded_message += char
        return decoded_message
