import qrcode

url = input('Ведите ссылку: ')

def get_qrcode(url, name='default'):
    qr = qrcode.make(data=url)
    qr.save(stream=f'{name}.png')

    return f'QR code создан имя {name}.png'

def main():
    print(get_qrcode(url, name='site'))

if __name__ == '__main__':
    main()
