# Riddle calculation
cats_legs = 3 * 4  # Legs on 3 cats
square_sides = 4   # Sides of a square
hand_fingers = 5   # Fingers on one hand

# Calculate the decryption key
decryption_key = (cats_legs / square_sides) * hand_fingers
shift = int(decryption_key)  # Ensure the shift value is an integer
print(f"Decryption Key (Shift Value): {shift}")

# Encrypted message
encrypted_message = "WTAAD LDGAS! LTARDBT ID IWT RPKT DC HTPHWDGT."

# Caesar Cipher Decryption
def caesar_decrypt(ciphertext, shift_value):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():  # Check if character is a letter
            ascii_offset = 65 if char.isupper() else 97
            # Shift character backward and wrap around using modulo
            decrypted_char = chr(((ord(char) - ascii_offset - shift_value) % 26) + ascii_offset)
            decrypted_text += decrypted_char
        else:
            # Non-alphabetic characters remain unchanged
            decrypted_text += char
    return decrypted_text

# Decrypt the message
decrypted_message = caesar_decrypt(encrypted_message, shift)
print(f"Decrypted Message: {decrypted_message}")
