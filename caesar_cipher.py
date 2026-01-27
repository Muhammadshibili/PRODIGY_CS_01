def caesar_cipher(text, shift, mode):
    result = ""
    shift = shift % 26

    for char in text:
        if char.isupper():
            base = ord('A')
            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += chr((ord(char) - base - shift) % 26 + base)

        elif char.islower():
            base = ord('a')
            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += chr((ord(char) - base - shift) % 26 + base)

        else:
            result += char

    return result


# ----------- User Interaction -----------
print("=" * 40)
print("        Caesar Cipher Tool")
print("=" * 40)

message = input("Enter your message: ")

try:
    shift = int(input("Enter shift value: "))
except ValueError:
    print("Shift must be a number")
    exit()

choice = input("Type 'e' for Encrypt or 'd' for Decrypt: ").lower()

if choice == 'e':
    mode = "encrypt"
elif choice == 'd':
    mode = "decrypt"
else:
    print("Invalid choice! Please type 'e' or 'd'")
    exit()

output = caesar_cipher(message, shift, mode)
print("Result:", output)