# Secure Image Steganography with XOR Encryption

This Python project demonstrates how to securely hide and reveal messages within images using **XOR encryption** and **Least Significant Bit (LSB) steganography**. The program ensures confidentiality by encrypting the message before embedding it into the image.

---

## Features
- **XOR Encryption**: Encrypts the message using a user-provided secret key.
- **LSB Steganography**: Embeds the encrypted message into the image's pixel data.
- **Error Handling**: Checks image size to ensure it can accommodate the message.
- **CLI Interface**: Easy-to-use command-line interface for hiding and revealing messages.

---

## Prerequisites
- Python 3.x
- OpenCV (`cv2`) library
- `struct` and `os` libraries (built-in with Python)

---

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/secure-steg.git
   cd secure-steg
Install the required libraries:

```bash
pip install opencv-python
```
## Usage
## 1. Hide a Message in an Image
Run the script and choose the hide option:h
```bash
python project.py
```
## Input the following:

Cover Image Path: Path to the image where the message will be hidden.

Secret Message: The message you want to hide.

Encryption Key: A secret key to encrypt the message.

## Example:
Hide(h) or reveal(r) message? (h/r): h
Enter cover image path: example.png
Enter secret message: This is a secret!
Create encryption key: mysecretkey
The program will create a new image (secret_image.png) with the hidden message.

## 2. Reveal a Hidden Message
Run the script and choose the reveal option:r

Input the following:

Secret Image Path: Path to the image with the hidden message.

Decryption Key: The secret key used during encryption.

## Example:

Hide(h) or reveal(r) message? (h/r): r
Enter secret image path: secret_image.png
Enter decryption key: mysecretkey
The program will decrypt and display the hidden message.

## Code Overview
Key Functions
hide_message(image_path, message, secret_key):

Encrypts the message using XOR encryption.

Embeds the encrypted message into the image using LSB steganography.

Saves the modified image as secret_image.png.

reveal_message(image_path):

Extracts the encrypted message from the image.

Decrypts the message using the provided secret key.

Displays the hidden message.

## Example
Input:
Cover Image: example.png

Secret Message: This is a secret!

Encryption Key: mysecretkey

Output:
Stego Image: secret_image.png (visually identical to the original image).

Revealed Message: This is a secret!

## Limitations
The image must be large enough to accommodate the message.

The secret key must be remembered for decryption.

## Future Scope
Add support for AES encryption for stronger security.

Develop a GUI for easier use.

Extend functionality to hide messages in audio and video files.
