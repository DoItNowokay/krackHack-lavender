from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt_message(public_key, message):
    cipher_text = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return cipher_text

def decrypt_message(private_key, cipher_text):
    plain_text = private_key.decrypt(
        cipher_text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plain_text.decode()

# Example usage:
# private_key, public_key = generate_key_pair()
# message = "Hello, world!"
# print(private_key,public_key)
# message='{"_id": "65c8d2ef7f85e5376ba99dc9", "name": "bila", "age": 10, "organ": "foot"}'
# cipher_text = encrypt_message(public_key, message)
# print("Encrypted message:", cipher_text.hex())
# plain_text = decrypt_message(private_key, cipher_text)
# print("Decrypted message:", plain_text)
