# CryptiGray Documentation

## Overview

CryptiGray is a web-based encryption system that combines BCD to Gray Code conversion with XOR key encryption for secure message transmission. It also includes PDF encryption capabilities, providing a comprehensive security solution for both text and document protection.

## Features

- **Text Encryption/Decryption**: Convert plain text to encrypted cipher using BCD → Gray Code transformation with XOR key encryption
- **PDF Encryption**: Password-protect PDF files with secure encryption
- **Educational Visualization**: Step-by-step visualization of the encryption/decryption process
- **User-Friendly Interface**: Modern, responsive design with animated elements
- **Cross-Platform**: Web-based solution accessible from any device with a browser

## Technical Implementation

### Backend (app.py)

The backend is built with Flask and handles:

- PDF encryption using PyPDF2
- File uploads and downloads
- Serving static files and templates

```python
from flask import Flask, render_template, request, jsonify, send_from_directory
from PyPDF2 import PdfReader, PdfWriter
import os
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder="static", template_folder="templates")
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Routes for serving pages
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/encrypt-page")
def encrypt_page():
    return render_template("encrypt.html")

@app.route("/decrypt-page")
def decrypt_page():
    return render_template("decrypt.html")

@app.route("/pdf-page")
def pdf_page():
    return render_template("pdf-encrypt.html")

# PDF encryption endpoint
@app.route("/encrypt", methods=["POST"])
def encrypt_pdf():
    # Handle PDF encryption logic
    pass

# File download endpoint
@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)
```

### Frontend Components

#### Index Page (index.html)
- Landing page with project information
- Team member showcase
- Navigation to encryption/decryption features

#### Encryption Page (encrypt.html)
- Interface for text encryption
- Real-time process visualization
- Copy/download functionality for encrypted text

#### Decryption Page (decrypt.html)
- Interface for text decryption
- Step-by-step decryption process display
- Security validation features

#### PDF Encryption Page (pdf-encrypt.html)
- Drag-and-drop PDF upload interface
- Password-based encryption
- Download functionality for encrypted PDFs

## Encryption Algorithm

### Text Encryption Process

1. **Character to ASCII**: Convert each character to its ASCII value
2. **Binary Conversion**: Convert ASCII to 8-bit binary representation
3. **Gray Code Conversion**: Transform binary to Gray code
4. **XOR Encryption**: Apply XOR operation with secret key
5. **Output**: Space-separated encrypted binary values

### Text Decryption Process

1. **XOR Decryption**: Reverse XOR operation with secret key
2. **Gray to Binary**: Convert Gray code back to binary
3. **ASCII Conversion**: Convert binary to ASCII values
4. **Character Reconstruction**: Rebuild original text from ASCII values

### PDF Encryption

Uses PyPDF2's encryption capabilities with user-provided passwords to secure PDF documents.

## Setup Instructions

### Prerequisites

- Python 3.7+
- Flask
- PyPDF2

### Installation

1. Clone or download the project files
2. Install required dependencies:
   ```bash
   pip install flask PyPDF2
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open a web browser and navigate to `http://localhost:5000`

## Usage Guide

### Text Encryption

1. Navigate to the Encryption page
2. Enter your message in the text area
3. Provide a secret key (minimum 3 characters)
4. Click "Encrypt Message"
5. Copy or download the encrypted output

### Text Decryption

1. Navigate to the Decryption page
2. Paste the encrypted binary text
3. Enter the same secret key used for encryption
4. Click "Decrypt Message"
5. View, copy, or download the decrypted text

### PDF Encryption

1. Navigate to the PDF Encryption page
2. Drag and drop a PDF file or click to select one
3. Enter a strong password
4. Click "Encrypt PDF"
5. Download the encrypted PDF file

## File Structure

```
project/
├── app.py                 # Flask application
├── templates/
│   ├── index.html        # Home page
│   ├── encrypt.html      # Text encryption page
│   ├── decrypt.html      # Text decryption page
│   └── pdf-encrypt.html  # PDF encryption page
├── static/
│   └── Assets/           # Team member images
├── uploads/              # Temporary file storage
└── README.md             # This documentation
```

## Security Considerations

- The same key must be used for encryption and decryption
- Keys are case-sensitive and must match exactly
- For maximum security, use long and complex keys
- PDF encryption uses standard PDF security mechanisms

## Browser Compatibility

CryptiGray works on all modern browsers including:
- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Team

- **Sarvan Kumar** - Team Lead
- **Manish Reddy** - Topic Researcher
- **Dheeraj** - UI/UX Designer

## License

© 2025 CryptiGray. All rights reserved.

## Support

For questions or issues, please contact the development team.
