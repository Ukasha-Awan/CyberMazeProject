# This is the Solution of CyberMaze- Cryptography level 1
# virtual machine | start machine | 
import itertools

encrypted_message_hex = "2b0910124614541507185502070e5f1b"

# Convert the hex message to bytes
encrypted_message = bytes.fromhex(encrypted_message_hex)

# Anna's personal details
details = ["fluffy", "15", "march", "john", "mary"]

# Function to perform XOR decryption
def xor_decrypt(encrypted, key):
    key = key.encode()  # Convert the key to bytes
    return bytes([encrypted[i] ^ key[i % len(key)] for i in range(len(encrypted))])

# Generate all possible key combinations
key_combinations = []
for r in range(1, len(details) + 1):
    key_combinations.extend([''.join(comb) for comb in itertools.permutations(details, r)])

# Try decrypting the message with each key
for key in key_combinations:
    try:
        decrypted_message = xor_decrypt(encrypted_message, key)
        # Attempt to decode the decrypted message as text
        plaintext = decrypted_message.decode('utf-8')
        print(f"Key: {key} => Decrypted Message: {plaintext}")
    except UnicodeDecodeError:
        continue
