def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text


def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            decrypted_char = chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text


def main():
    message = input("Enter a message to encrypt: ")
    shift = int(input("Enter the shift value: "))

    encrypted_message = caesar_cipher_encrypt(message, shift)
    print("Encrypted message:", encrypted_message)

    decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
    print("Decrypted message:", decrypted_message)


if __name__ == "__main__":
    main()

