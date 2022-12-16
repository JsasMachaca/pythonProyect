import time
import random

def numpares():
    i = 1
    m = 0
    print (i)
    l = 1
    while l < 11:
        l+= 1
        f = i + m
        m = i
        i = f
        time.sleep(2)
        print(i)

def cuadro(Caracter, filas, columnas):
    for i in range (filas-2):
        print (Caracter + '  '*(columnas-2) + Caracter )

#cuadro("+", 8, 10)
numpares()









