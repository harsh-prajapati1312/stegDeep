# stegDeep - Advanced Steganography Tool

stegDeep is a powerful steganography tool designed to hide and extract secret messages or files within images. It supports various image formats and includes functionality to detect hidden steganographic data. This tool is ideal for cybersecurity enthusiasts, penetration testers, and privacy-focused users.

## Disclaimer

This tool is intended solely for educational and research purposes. Using steganography techniques to conceal or transmit illicit information may violate laws and regulations in your jurisdiction. The author and contributors are not responsible for any misuse of this tool.

## Features

- **Banner Display**: Shows a custom banner when executed.
- **Hide Text in Images**: Embed secret text messages within images.
- **Extract Hidden Text**: Retrieve embedded text from modified images.
- **Hide Files in Images**: Embed any type of file (e.g., documents, media) inside an image.
- **Extract Files from Images**: Retrieve embedded files and restore them to their original form.
- **Steganography Detection**: Scan images to determine if they contain hidden data.
- **Supports Multiple Image Formats**: Works with PNG, JPEG, BMP, and more.

## Requirements

- Python 3.x (Recommended: 3.6+)
- Required Python packages:
  - OpenCV (`opencv-python`)
  - NumPy (`numpy`)
  - PIL (`pillow`)

## Installation

Clone the repository from GitHub using:

```bash
git clone https://github.com/harsh-prajapati1312/stegDeep.git
cd stegDeep
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage/Examples

### Hide a Text Message
```bash
python stegno.py --hide --source image.png --text "Secret Message"
```

### Extract a Hidden Text Message
```bash
python stegno.py --extract --source image_embedded.png
```

### Hide a File inside an Image
```bash
python stegno.py --hide-file --source image.png --file secret.txt
```

### Extract a Hidden File
```bash
python stegno.py --extract-file --source image_embedded.png --file output.txt
```

### Detect Steganography in an Image
```bash
python stegno.py --detect --source image_embedded.png
```

## Security Considerations

- **Data Privacy**: Ensure sensitive data is handled securely when using this tool.
- **Forensic Analysis**: Some steganography detection tools can identify modified images.
- **Legal Compliance**: Verify the legal implications of using steganography in your country.

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://harsh-prajapati1312.github.io/myportfolio/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/harshprajapati13)


## Authors

- Developed and maintained by: **Harshkumar Prajapati**

## License

This project is licensed under the MIT [License](./LICENSE) - see the LICENSE file for details.

