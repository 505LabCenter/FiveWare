import os
import sys
import subprocess

# Auto install required module
def install_module(module_name):
    subprocess.check_call([sys.executable, "-m", "pip3", "install", module_name])

# Install cryptography module if not already installed
try:
    from cryptography.fernet import Fernet
except ImportError:
    install_module("cryptography")
    from cryptography.fernet import Fernet

# Load the encryption key from keys.five
def load_key():
    return open("keys.five", "rb").read()

# Decrypt files in the specified directory
def decrypt_files(directory):
    key = load_key()
    fernet = Fernet(key)
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as file_data:
                data = file_data.read()
            decrypted_data = fernet.decrypt(data)
            with open(file_path, "wb") as file_data:
                file_data.write(decrypted_data)

# Main function to run the decryption
def main():
    directory = input("Masukkan direktori yang ingin didekripsi: ")
    decrypt_files(directory)
    print("File telah didekripsi.")

if __name__ == "__main__":
    main()

