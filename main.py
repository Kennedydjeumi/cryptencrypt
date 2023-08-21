from cryptography.fernet import Fernet

# Generate a random encryption key
key = Fernet.generate_key()

Encrypted_object = Fernet(key)

Original_data = "Dont decrypt this very important message"

# Encrypt the original data
encrypted_og_data = Encrypted_object.encrypt(Original_data.encode())

# Print the original data
print("Original data: " + Original_data)

# Try to print the encrypted data, handling TypeError if it occurs
try:
    print("Encrypted mode: " + encrypted_og_data.decode())
except TypeError:
    print("Something wrong happened while trying to print encrypted data")

# Try to decrypt the encrypted data, handling AttributeError if it occurs
try:
    decrypted_og_data = Encrypted_object.decrypt(encrypted_og_data).decode()
    print("Decrypted data: " + decrypted_og_data)
except AttributeError:
    print("Attribute error while trying to decrypt the data")
