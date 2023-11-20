import qrcode

# List of image URLs and their descriptions
images_info = [
    {'url': 'https://github.com/Gyimah3/QR_CODE/blob/main/modified_image_1.png?raw=true', 'description': 'RCEES CHAIR'},
    {'url': 'https://github.com/Gyimah3/QR_CODE/blob/main/modified_image_0.png?raw=true', 'description': 'RCEES CHAIR'}
    
]

# Loop through each URL and description and generate a QR code
for i, info in enumerate(images_info):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Combine URL and description
    data = f"{info['url']}\n{info['description']}"
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f'qr_code_{i}.png')
