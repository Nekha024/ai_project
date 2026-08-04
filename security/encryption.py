from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)


def encrypt_data(data):
    return cipher.encrypt(data.encode())


def decrypt_data(token):
    return cipher.decrypt(token).decode()


if __name__ == "__main__":

    text = "Interview Transcript"

    encrypted = encrypt_data(text)
    print("Encrypted:", encrypted)

    decrypted = decrypt_data(encrypted)
    print("Decrypted:", decrypted)