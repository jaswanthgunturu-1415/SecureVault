# 🔐 SecureVault – Secure File Encryption and Decryption System
## 🚀 Live Demo
[Open SecureVault Application](https://securevault-z45bprm6pucghgsql7p3kk.streamlit.app/)

## 📌 Description
SecureVault is a Python-based cybersecurity project designed to protect confidential files using AES-256-GCM encryption. It uses Scrypt for password-based key derivation and provides a simple Streamlit web interface for encrypting and decrypting files securely.

## ✨ Features
- 🔒 AES-256-GCM authenticated encryption
- 🔑 Password-based key derivation using Scrypt
- 📁 File encryption and decryption
- 🛡️ Detection of incorrect passwords and modified encrypted files
- 🔍 SHA-256 file integrity verification
- 📥 Download encrypted and decrypted files
- 🧪 Automated testing using Pytest

## 🛠️ Technologies Used
- Python
- Streamlit
- Cryptography
- Pytest

## ⚙️ Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/SecureVault.git
cd SecureVault
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to use the application.

## 🧪 Run Tests
```bash
pytest -v
```

## 🔐 Security
- Use a strong password of at least 12 characters.
- Keep your encryption password safe.
- Never upload confidential files or passwords to a public repository.

## 🎯 Project Objective
To demonstrate secure file handling through authenticated encryption, password-based key derivation, and file integrity verification.

## 👨‍💻 Author
**Jaswanth**

## 📚 Disclaimer
This project is intended for educational purposes and cybersecurity learning.
