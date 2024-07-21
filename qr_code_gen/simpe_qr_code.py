import qrcode


data = "<< Your webiste link >>"
qr = qrcode.QRCode(version=1,
                   box_size=7,
                   border=3
                   )
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill_color='blue',
                      back_color='white')
image.save('Website_image.png')
