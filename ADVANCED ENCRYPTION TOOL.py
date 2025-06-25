#ADVANCED ENCRYPTION TOOL

from cryptography.fernet import Fernet
import os

# -------------------------
# Generate AES Key and Save to File
# -------------------------
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("\n✅ AES Key generated and saved to 'secret.key'")

# -------------------------
# Load AES Key from File
# -------------------------
def load_key():
    return open("secret.key", "rb").read()

# -------------------------
# Encrypt File
# -------------------------
def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted = fernet.encrypt(data)

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)

    print(f"\n🔒 File '{filename}' encrypted successfully as '{filename}.enc'")

# -------------------------
# Decrypt File
# -------------------------
def decrypt_file(encrypted_filename):
    key = load_key()
    fernet = Fernet(key)

    with open(encrypted_filename, "rb") as file:
        encrypted_data = file.read()

    decrypted = fernet.decrypt(encrypted_data)

    output_file = encrypted_filename.replace(".enc", ".dec")
    with open(output_file, "wb") as file:
        file.write(decrypted)

    print(f"\n🔓 File '{encrypted_filename}' decrypted successfully as '{output_file}'")

# -------------------------
# User-Friendly Terminal Menu
# -------------------------
def main():
    print("""
    ===============================
      File Encryption Tool (AES-256)
    ===============================
    1. Generate New AES Key
    2. Encrypt File
    3. Decrypt File
    """)

    choice = input("Select an option (1/2/3): ")

    if choice == "1":
        generate_key()

    elif choice == "2":
        filename = input("Enter the filename to encrypt: ")
        if os.path.exists(filename):
            encrypt_file(filename)
        else:
            print("❌ File not found!")

    elif choice == "3":
        filename = input("Enter the encrypted filename to decrypt: ")
        if os.path.exists(filename):
            decrypt_file(filename)
        else:
            print("❌ File not found!")

    else:
        print("Invalid choice. Exiting...")

if __name__ == "__main__":
    main()
