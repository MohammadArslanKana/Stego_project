import cv2
import os
import struct

def hide_message(image_path, message, secret_key):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Couldn't load image")
        return

    # Encrypt message using XOR with secret key
    encrypted_data = []
    key_len = len(secret_key)
    for i, char in enumerate(message):#Each char represents one character from the secret messag
        key_char = secret_key[i % key_len]#if key is hsorter then message then it makes it loop from start again of the key
        encrypted_data.append(ord(char) ^ ord(key_char))#ord(char): Converts the message character to its ASCII value.
                                                        #ord(key_char): Converts the corresponding key character to its ASCII value.

    # Add message length header
    data_length = len(encrypted_data)
    length_header = struct.pack('!I', data_length)

    # Embed data in image
    row, col, channel = 0, 0, 0
    img_row, img_col, _ = img.shape
    
    # Store length header , The first few pixels store the message length
    for byte in length_header:
        if row >= img_row or col >= img_col:
            print("Error: Image too small")
            return
        img[row, col, channel] = byte
        row += 1
        col += 1
        channel = (channel + 1) % 3

    # Store encrypted message
    for byte in encrypted_data:
        if row >= img_row or col >= img_col:
            print("Error: Image too small")
            return
        img[row, col, channel] = byte
        row += 1
        col += 1
        channel = (channel + 1) % 3

    cv2.imwrite("secret_image.png", img)
    print("Message hidden in secret_image.png")
    os.system("start secret_image.png")

def reveal_message(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Couldn't load image")
        return

    row, col, channel = 0, 0, 0
    img_row, img_col, _ = img.shape
    
    # Read length header
    length_bytes = []
    for _ in range(4):
        if row >= img_row or col >= img_col:
            print("Error: Invalid image format")
            return
        length_bytes.append(img[row, col, channel])
        row += 1
        col += 1
        channel = (channel + 1) % 3

    data_length = struct.unpack('!I', bytes(length_bytes))[0]

    # Read encrypted data
    encrypted_data = []
    for _ in range(data_length):
        if row >= img_row or col >= img_col:
            print("Error: Data corrupted")
            return
        encrypted_data.append(img[row, col, channel])
        row += 1
        col += 1
        channel = (channel + 1) % 3

    # Decrypt message
    secret_key = input("Enter decryption key: ")
    decrypted = []
    key_len = len(secret_key)
    for i, byte in enumerate(encrypted_data):
        key_char = secret_key[i % key_len]
        decrypted.append(chr(byte ^ ord(key_char)))

    print("Hidden message:", ''.join(decrypted))

# Main program
choice = input("Hide(h) or reveal(r) message? (h/r): ").lower()
if choice == 'h':
    img_path = input("Enter cover image path: ")
    msg = input("Enter secret message: ")
    key = input("Create encryption key: ")
    hide_message(img_path, msg, key)
elif choice == 'r':
    img_path = input("Enter secret image path: ")
    reveal_message(img_path)
else:
    print("Invalid choice")




