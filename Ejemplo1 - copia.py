import time
print("cargando...")
def barra(caracter):
    for i in range (20):
        time.sleep(0.5)
        print(caracter, end="")
barra("=")

def pepe():
    time.sleep(3)
    print ("\n TE AMO  ")


file = open("D:\hola.txt", "a")
file.write("holiwis ")
file.close()