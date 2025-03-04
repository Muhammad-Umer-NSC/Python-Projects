import qrcode
import validators

def main():
    text = url_checker()
    file = input("Enter name: ")
    generate_qr_code(file, text)

def url_checker():
    while True:
        text = input("Enter URL: ")
        url =  validators.url(text)
        if url:
            return text
        else:
            print("Enter correct URL e.g. https://something.com")

def generate_qr_code(file, text):
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="green", back_color="black")
    img.save(file + ".png")

if __name__ == "__main__":
    main()