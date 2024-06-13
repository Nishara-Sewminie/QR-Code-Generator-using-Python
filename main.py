import qrcode
import image
qr = qrcode.QRCode(
    version= 10,
    box_size= 10,
    border= 5
)

data = "https://github.com/Nishara-Sewminie/QR-Code-Generator-using-Python"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black",back_color="white")
img.save("test2.png")
