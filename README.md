
# Image Text Overlay and QR Code Generator
## Introduction
This project comprises two main components: a script for adding custom text overlays to images (add_image.py) and another script for generating QR codes (QR_CODE.py) that link to these images hosted on GitHub. The combination of these two functionalities allows for a unique way of sharing images with embedded messages, accessible via QR codes.

## Features
**Text Overlay on Images**: Add custom descriptions or messages directly onto your images.
**QR Code Generation**: Create QR codes that link to your modified images, making them easily shareable and accessible.
GitHub Image Hosting: Leverage GitHub's reliable platform for hosting your images and ensuring they are always accessible via QR codes.

## Components
**Text Overlay Script (add_image.py)**: This script takes local images and adds specified text messages onto them. It's perfect for labeling images, adding descriptions, or embedding any text-based information directly onto the image.

**QR Code Generator Script (QR_CODE.py)**: After hosting your images on GitHub, this script generates QR codes for each image URL. These QR codes can be scanned to view the images, making it extremely convenient to share and access them.

# Usage
## Setting Up
Clone the Repository:


Copy code
git clone [repository URL]
cd [Gyimah3]

## Install Dependencies:
Make sure you have Python installed and then set up a virtual environment:


**Copy code**
- Windows:
        
        python -m venv venv; venv\Scripts\activate

## Running the Scripts
**Adding Text to Images:**
- Run the demo this (being at the repository root):

        add_image.py

## Generating QR Codes:
After uploading the modified images to GitHub, edit QR_CODE.py with the URLs of these images. Then run:
- Run the this (being at the repository root):

        QR_CODE.py

This will Create QR code.

Generating QR Codes:
After uploading the modified images to GitHub, edit qr_code_generator.py with the URLs of these images. Then run:

Copy code
python qr_code_generator.py
This will generate QR codes linking to
