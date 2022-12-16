import qrcode
def qr():
    i = qrcode.make("192.168.1.3:8000")
    o = open("hola.png", "wb")
    i.save(o)
    i.close()

lista = [1,2,3,4,5,6,7,8,9,10]
for l in lista:
    print(l)
