def linea():
    print('=' * 35)
    print ('      Seleccione su opcion')
    print('=' * 35)
    print ('   Opcion 1 : Ingresar productos')
    print ('   Opcion 2 : Mostrar productos')
    print ('   Opcion 3 : Agregar al stock')
    print ('   Opcion 4 : Vender')
    print ('   Opcion 5 : Salir')
    print('=' * 35)
#--------Diccionarios y listas para almacenar los productos,stock,precios y almacenar el total a vender----------------
Productos = {}
Stock={}
Vender=[]
total=0
suma=0
linea()
opcion = int(input('  Ingrese su opción: '))

while 1 > 0:
#----------------------------------Cuando se ingrese la opción 1------------------------------------------------------
    if opcion == 1 :
        producto = input ('  Ingrese el producto:')
        Precio= float(input('  Ingrese el precio del producto: '))
        stock = int(input ('  Ingrese las unidades :'))
        Productos[producto]=Precio
        Stock[producto]=stock
        print()
        print('  FINALIZADO')
        print()
        linea()
        opcion = int(input('  Ingrese su opción: '))

#-------------------------------Cunado se ingrese la opción 2---------------------------------------------------------
    elif opcion == 2 :
        for k, v in Productos.items():
            print(k,v,)
        print()
        print('  FINZALIZADO')
        print()
        linea()
        opcion = int(input('  Ingrese su opción: '))

#--------------------------------Cunado se ingrese la opción 3--------------------------------------------------------
    elif opcion == 3:
        prod=input('  a que producto desea agregar: ')
        if prod in Stock:
            cantidad = int(input('  Cuantas unidades desea agregar: '))
            p=Stock[prod]
            p+=cantidad
            Stock[prod]=p
            print(' ',prod,':',p)
            print('  Producto agregado')
            print()
            print('  FINALIZADO')
            print()
        else:
            print('  Lo siento este producto no se encuentra dentro del almacen')
        linea()
        opcion = int(input('  Ingrese su opción: '))

#------------------------------------Cunado se ingrese la opción 4----------------------------------------------------
    elif opcion == 4:
        ven=int(input('  Cuantos productos desea vender: '))
        for i in range(ven):
            v=input('  Que producto(s) venderá: ')
            if v in Stock:
                c = int(input('  Cuantos venderá:'))
                a=Stock[v]
                a-=c
                #Stock[v]=a
                b=Productos[v]
                print(  v,'vendido, se quito del almacen',c,'unidades')
                print('  Hay',a,'unidades de:',v)
                t=b*c
                Vender.append(t)
                suma+=t
                print(Vender)
                print('  El total a pagar es:',suma)
            else:
                print('  Lo siento este producto no se encuentra dentro del almacen')
        del Vender[0:30]
        print()
        print('  FINALIZADO')
        print()
        linea()
        opcion = int(input('  Ingrese su opción: '))

#----------------------------------------Cunado se ingrese la opción 5-------------------------------------------------
    elif opcion == 5:
        break
print()
print('  HASTA LUEGO')



