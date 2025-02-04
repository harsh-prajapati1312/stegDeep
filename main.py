import binascii
import cv2
import numpy as np
import zlib
import base64
import argparse
import os
from PIL import Image

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    ███████╗████████╗███████╗ ██████╗ ██████╗ ███████╗███████╗██████╗ 
    ██╔════╝╚══██╔══╝██╔════╝██╔════╝ ██╔══██╗██╔════╝██╔════╝██╔══██╗
    ███████╗   ██║   █████╗  ██║  ███╗██║  ██║█████╗  █████╗  ██████╔╝
    ╚════██║   ██║   ██╔══╝  ██║   ██║██║  ██║██╔══╝  ██╔══╝  ██╔═══╝ 
    ███████║   ██║   ███████╗╚██████╔╝██████╔╝███████╗███████╗██║     
    ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝     
    
    stegDeep - Advanced Steganography Tool
    """)

def hide_text(image_path, message):
    img = cv2.imread(image_path)
    message = zlib.compress(message.encode('utf-8'))
    message_bits = ''.join(format(byte, '08b') for byte in message)
    
    if len(message_bits) > img.size:
        raise ValueError("Message is too large to hide in this image!")
    
    flat_img = img.flatten()
    for i in range(len(message_bits)):
        flat_img[i] = (flat_img[i] & 254) | int(message_bits[i])
    
    img = flat_img.reshape(img.shape)
    output_path = os.path.splitext(image_path)[0] + '_embedded.png'
    cv2.imwrite(output_path, img)
    print(f"Message hidden in: {output_path}")

def extract_text(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Unable to read the image file '{image_path}'. Check the file path and format.")
        return None
    
    flat_img = img.flatten()
    message_bits = ''.join(str(flat_img[i] & 1) for i in range(flat_img.size))
    
    byte_array = bytearray(int(message_bits[i:i+8], 2) for i in range(0, len(message_bits), 8))
    try:
        message = zlib.decompress(byte_array).decode('utf-8')
        print("Extracted Message:", message)
        return message
    except:
        print("No valid hidden message found!")
        return None

def extract_file(image_path, output_path):
    hidden_data = extract_text(image_path)
    if hidden_data:
        try:
            hidden_data = hidden_data.strip()  # Remove unwanted spaces or newlines
            if len(hidden_data) % 4:
                hidden_data += '=' * (4 - len(hidden_data) % 4)  # Properly pad base64 data
            decoded_data = base64.b64decode(hidden_data)
            decompressed_data = zlib.decompress(decoded_data)
            with open(output_path, 'wb') as f:
                f.write(decompressed_data)
            print(f"Extracted file saved as {output_path}")
        except (binascii.Error, zlib.error) as e:
            print(f"Error during extraction: {e}")
    else:
        print("Extraction failed. No valid data found in the image.")

def hide_file(image_path, file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    compressed_data = zlib.compress(file_data)
    hide_text(image_path, base64.b64encode(compressed_data).decode('utf-8'))
    print(f"File {file_path} hidden inside {image_path}")

# def extract_file(image_path, output_path):
#     hidden_data = extract_text(image_path)
#     if hidden_data:
#         with open(output_path, 'wb') as f:
#             f.write(zlib.decompress(base64.b64decode(hidden_data)))
#         print(f"Extracted file saved as {output_path}")

def detect_steganography(image_path):
    img = cv2.imread(image_path)
    flat_img = img.flatten()
    modified_bits = sum(1 for i in flat_img if i & 1)
    print(f"Potential hidden data detected: {modified_bits} bits altered")

def parse_arguments():
    parser = argparse.ArgumentParser(description="stegDeep - Advanced Steganography Tool")
    parser.add_argument('--hide', action='store_true', help='Hide a message in an image')
    parser.add_argument('--extract', action='store_true', help='Extract a hidden message from an image')
    parser.add_argument('--hide-file', action='store_true', help='Hide a file inside an image')
    parser.add_argument('--extract-file', action='store_true', help='Extract a hidden file from an image')
    parser.add_argument('--detect', action='store_true', help='Detect if an image contains hidden data')
    parser.add_argument('--source', type=str, required=True, help='Source image path')
    parser.add_argument('--file', type=str, help='File path for hiding or extracting')
    parser.add_argument('--text', type=str, help='Message to hide')
    
    example_usage = """
    Examples:
    Hide a text message:\n
        \tpython main.py --hide --source image.png --text "Secret Message"
    Extract a text message:\n
        \tpython main.py --extract --source image_embedded.png
    Hide a file:\n
        \tpython main.py --hide-file --source image.png --file secret.txt
    Extract a file:\n
        \tpython main.py --extract-file --source image_embedded.png --file output.txt
    Detect steganography:\n
        \tpython main.py --detect --source image_embedded.png
    """
    parser.epilog = example_usage
    return parser.parse_args()

def main():
    print_banner()
    args = parse_arguments()
    
    if args.hide and args.text:
        hide_text(args.source, args.text)
    elif args.extract:
        extract_text(args.source)
    elif args.hide_file and args.file:
        hide_file(args.source, args.file)
    elif args.extract_file and args.file:
        extract_file(args.source, args.file)
    elif args.detect:
        detect_steganography(args.source)
    else:
        print("Invalid usage! Use --help for options.")

if __name__ == "__main__":
    main()