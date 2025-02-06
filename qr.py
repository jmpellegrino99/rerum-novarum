import qrcode

# Data to encode
data = "https://www.example.com"

# Create a QR Code object
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level (L is lowest)
    box_size=10,  # size of each box in the QR Code
    border=4,  # width of the border (number of boxes)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the image as a PNG file
img.save("qr_code.png")

# Optionally, show the image
img.show()

