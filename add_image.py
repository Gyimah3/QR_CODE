from PIL import Image, ImageDraw, ImageFont
import qrcode

images_info = [
    {'path': '9a6bdfcf-1687-4f42-b165-4fe1289378cb.jpg', 'description': 'RCEES CHAIR A'},
    {'path': 'eecb6594-7994-4fb6-8876-025fd0e7d676.jpg', 'description': 'RCEES TABLE A'}
   
]

for i, info in enumerate(images_info):
    img = Image.open(info['path'])
    font = ImageFont.truetype("arial.ttf", size=70)
    draw = ImageDraw.Draw(img)
    # Fixed position 
    text_position = (70, 30)  
    draw.text(text_position, info['description'], font=font, fill="white")
    modified_image_path = f'modified_image_{i}.png'
    img.save(modified_image_path)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(modified_image_path)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_image_path = f'qr_code_{i}.png'
    qr_img.save(qr_image_path)
