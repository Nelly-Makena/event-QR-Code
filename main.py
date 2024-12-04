import pyqrcode


def generate_qr_code(url, filename):

    qr = pyqrcode.create(url)  # Create QR code
    qr.png(filename, scale=10)  # Save as PNG with high resolution
    print(f"QR Code successfully saved as {filename}")


event_link =" https://forms.gle/dDDh2EChkMcV6VHW9" # Replace with your actual URL
filename = "event_qr_code.png"  # Desired filename for the QR code
generate_qr_code(event_link, filename)
