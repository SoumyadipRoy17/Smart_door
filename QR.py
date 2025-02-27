import qrcode
from secret_key import key, registered_users  # Import from secret_key.py

# Format the data for the QR code
data = f"Key: {key}\nRegistered Users: {', '.join(registered_users)}"

# Create a QR code object
qr = qrcode.QRCode(
    version=1,  # Adjust size (1 is smallest, can increase if needed)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
    box_size=10,  # Each box in QR is 10x10 pixels
    border=4  # Border size around the QR code
)
qr.add_data(data)  # Add the formatted data
qr.make(fit=True)

# Generate QR code image
qr_img = qr.make_image(fill="black", back_color="white")

# Save QR code as an image
qr_img.save("secret_key_qr.png")

print("[✅] QR Code generated successfully and saved as 'secret_key_qr.png'")
