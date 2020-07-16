# En este archivo se ejecutan la funciones que se nececitam
# recibe un entero por input y determina si es primo o no
def Primo (n):

    NumeroFinal=0  # guarda el numero que comparamos
    i=1
    while i<n:
        if n%i==0:
            NumeroFinal=i
        i+=1
    if NumeroFinal==1:
        print(f"el numero {n} es primo ")
    else:
        print(f"el numero {n} NO es primo")
    return NumeroFinal
# Escribir la opcion en el menu
def Opcion (posicion ,nombre):
      print (f"Elige {posicion} para ejecutar la funcion {nombre}")
      return
# Genera un input para llamar valores
def Entrada ():
    a= float(input("digite su Numero ......"))
    return a
# Funcion Tabla de Multiplicar
def Multiplicar(n):
    print("la tabla del el "+ str(n))
    for i in range(10):
        print(f" {i} x {n} = {n*i}")
    return n
#funcion de fiboncci
def Fibonacci(n):
    iUno=1
    iCero=0
    i=1
    if n==0 :
        print(1)
    else:
        print(1)
        while i< n:
            i+=1
            iDos=iUno +iCero
            iCero=iUno
            iUno=iDos
            print(iDos)
# funcion genera una lista hasta que se ingrese0
def Lista():
    lista=[]
    inicio=True
    while inicio:
        elemento= int(input("digite su elemento de la lista "))
        if elemento!=0:
            lista.append(elemento)
        elif elemento == 0:
            inicio=False
    print(lista)
# funcion dado una lista de numero debuelve el maxio y el minimo
def Maximo():
    NumeroMaxino=0
    NumeroMinimo=0
    Final=True
    print("dgita una lista de naturales y digita el cero para terminar ")
    while Final:
        Numero=int(input("digita tu numero "))
        if Numero >= NumeroMaxino:
            NumeroMaxino=Numero
        if Numero <= NumeroMinimo:
            NumeroMinimo=Numero
        if Numero== 0 :
            print("salirrrr")
            Final = False
    print("/////////////////////////////")
    print("el numero mayor   es    " + str(NumeroMaxino) + "    el numero menor es   "+ str(NumeroMinimo))
    print("/////////////////////////////")
def PrimoEnesimo (CantidadFinal):
    Cantidad=0
    j=1

    while Cantidad!=CantidadFinal:

        NumeroFinal=0  # guarda el numero que comparamos
        i=1
        while i<j:
            if j%i==0:

                NumeroFinal=i
            i+=1
        if NumeroFinal==1:
            print(f"el numero {j} es primo ")
            Cantidad=Cantidad+1
        j=j+1
