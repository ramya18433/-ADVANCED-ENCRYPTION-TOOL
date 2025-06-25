# -ADVANCED-ENCRYPTION-TOOL

*company : CODETECH IT SOLUTION

*NAME* : Meesala Ramya

*INTERN ID * : CT04DF610

*DOMAIN * :CYBER SECURITY AND ETHICAL HACKING 

DURATION  : 4 WEEKS 

MENTER  : NEELA SANTOSH

## ADVANCED ENCRYPTION TOOL

This project presents a Python-based file encryption and decryption tool that uses the AES-256 standard for securing files. Designed for simplicity and robustness, this tool allows users to encrypt sensitive files and decrypt them when required, using a secure, automatically generated key. The tool is implemented using Python’s cryptography library, which is known for providing strong, reliable cryptographic functions suitable for real-world security applications.

The primary purpose of this tool is to provide users with an easy, reliable way to protect their files from unauthorized access. Whether you need to secure personal documents, confidential reports, or any sensitive data, this tool ensures your files are encrypted using industry-standard AES-256 encryption. The tool supports a variety of file types, including text files, documents, images, and more.

The encryption process works by first generating a symmetric AES key, which is saved locally in a file called secret.key. This key is essential for both encryption and decryption processes and must be kept secure by the user. Without this key, decryption is not possible, ensuring that unauthorized users cannot access the contents of encrypted files.

The tool features a simple, user-friendly command-line interface. Users can choose to generate a new AES key, encrypt a file, or decrypt a previously encrypted file through a straightforward menu-driven system. The process is highly interactive, guiding the user step by step, making it accessible even to those with minimal technical experience.

When encrypting a file, the tool reads the original file’s contents in binary mode and applies AES encryption using the saved key. The resulting encrypted file is saved with a .enc extension to clearly differentiate it from unencrypted files. Similarly, during decryption, the tool takes an encrypted .enc file and restores its original content, saving it with a .dec extension.

This tool demonstrates best practices in file security, emphasizing the importance of key management. Users are advised to store the secret.key file in a safe location, as losing this file renders encrypted files unrecoverable. The project intentionally focuses on educational use, introducing students, developers, and security enthusiasts to encryption concepts in an approachable, hands-on manner.

Additionally, this project is designed with modularity in mind, allowing future expansion. Features such as password-protected decryption, graphical user interfaces, or support for batch file encryption can be easily added. By providing a clear code structure and leveraging widely accepted libraries, this tool serves as a strong foundation for anyone interested in building more advanced encryption applications.

In conclusion, this AES-256 File Encryption & Decryption tool combines security, simplicity, and extensibility. It offers users an effective way to protect their data while promoting better understanding of real-world cryptography techniques. This project is ideal for academic demonstrations, self-learning, or basic file protection in everyday use.

##🔐 Advanced File Encryption Tool
A secure file encryption and decryption tool built using Python and Tkinter. It leverages AES-256 encryption with PBKDF2 key derivation to provide strong protection for your files.

📦 Features
AES-256 encryption using CBC mode
Secure password-based key derivation (PBKDF2 with SHA-256)
Random salt and IV for each encryption
Graphical User Interface (GUI) built with Tkinter
Automatic padding and depadding (PKCS7)
Easy-to-use file selection dialogs
Error handling with user-friendly messages
🛠️ Installation
Clone the repository:

cd encryption_tool
Install dependencies:

pip install cryptography
🚀 Usage
Run the application:

python encryption_tool.py
GUI Options:
Encrypt File: Select any file you want to encrypt. Enter a strong password when prompted. The output will be saved as filename.ext.enc.
Decrypt File: Select an .enc file. Enter the password used during encryption. The decrypted file will be saved as filename.ext.dec.
🧠 How It Works
A random 16-byte salt and IV are generated for each encryption.
A secure 256-bit key is derived from the password using PBKDF2 with 100,000 iterations.
Data is encrypted using AES-CBC and padded to a multiple of 16 bytes.
Decryption reverses the process using the original salt and IV from the encrypted file.
🔐 Security Notes
Always use a strong password.
This tool does not store or transmit your password.
If the password is lost, the encrypted data cannot be recovered.
📁 File Structure
encryption_tool.py   # Main GUI and logic script
README.md            # Project documentation
