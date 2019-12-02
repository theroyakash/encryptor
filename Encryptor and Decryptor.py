from cryptography.fernet import Fernet

# Generate a key:
generatedKey = Fernet.generate_key()
print(generatedKey)

# Saving a key to a file on desktop so that message can be decrypted later on:
file = open('UseAsKey.keyFile', 'wb')  # Writes bytes in a file of dot keyFile Ext.
file.write(generatedKey)  # Key is type bytes
file.close()

# Getting input from the User to encrypt:
message = input("Give me a damn Input that I can encrypt")

# Encrypting the message:
encoded_message = message.encode()
fernet_key = Fernet(generatedKey)
encrypted_text = fernet_key.encrypt(encoded_message)

decoded_encrypted_text = encrypted_text.decode()

print(message)  # Displays what I typed
print(decoded_encrypted_text)  # Displays what computer encrypted.

# Decryption:

from cryptography.fernet import Fernet

readKey = input(b'What is your encryption Key? ')

# Type what you see in the encrypted message:
encrypted_text = input("Type what you see in the encrypted message: ")

fernet_key = Fernet(readKey)
decrypted_text = fernet_key.decrypt(encrypted_text)

decoded_decrypted_text = decrypted_text.decode()
print("Your decrypted message is: ", decoded_decrypted_text)
