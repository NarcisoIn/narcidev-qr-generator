import qrcode 

url = input("Ingresa el URL que deseas convertir en código QR: ")

archivo = input("Ingresa el nombre del archivo donde deseas guardar el código QR (con extensión .png): ")

qr = qrcode.QRCode (
    version = 1,
    box_size = 10,
    border=5
)

qr.add_data(url)

qr.make(fit=True)

imagen = qr.make_image(fill="black", back_color="white")

imagen.save(archivo)
