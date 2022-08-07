
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    def encrypt(plain_text, shift_amount):
        encryptedWord = ""

        for letter in plain_text:
            alphabetIndex = int(alphabet.index(letter)) + shift_amount
            encryptedWord += alphabet[alphabetIndex]
        
        return encryptedWord
    
    wordEncrypted = encrypt(text, shift)
    print(wordEncrypted)

if direction == 'decode':
    def decrypt(plain_text, shift_amount):
        encryptedWord = ""

        for letter in plain_text:
            alphabetIndex = int(alphabet.index(letter)) - shift_amount
            encryptedWord += alphabet[alphabetIndex]
        
        return encryptedWord

    wordEncrypted = decrypt(text, shift)
    print(wordEncrypted)
