# Caesar Cipher Encryption and Decryption

def caesar_cipher(text, shift, mode):
    result = ""
    shift = shift % 26  # Ensure shift value stays within 0–25

    for char in text:
        if char.isalpha():  # Only encrypt letters
            base = ord('A') if char.isupper() else ord('a')
            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == "decrypt":
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char  # Keep non-letters unchanged
    return result


# --- Main Section ---
print("=== Caesar Cipher Encryption and Decryption ===")
message = input("Enter your message: ")
shift = int(input("Enter the shift value: "))
mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

if mode in ['encrypt', 'decrypt']:
    output = caesar_cipher(message, shift, mode)
    print(f"\n{mode.title()}ed Message: {output}")
else:
    print("Invalid mode! Please enter 'encrypt' or 'decrypt'.")
