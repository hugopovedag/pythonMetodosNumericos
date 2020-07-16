# En este documento es la pagina prinsipal de la
# calculadora
import Funciones as fun


print("Bienbenido a tu Calculadora ")
print("///////////////////////////// ")

Salir= True
while Salir:
    fun.Opcion(0,"Salir")
    fun.Opcion(1,"Primo")
    fun.Opcion(2,"Multiplicar")
    fun.Opcion(3,"Fibonacci")
    fun.Opcion(4,"Lista")
    fun.Opcion(5,"Maximo")
    fun.Opcion(6,"Numero Primos")
    print("///////////////////////////////////////////")
    Eleccion=int(input("Digita la opcion que deseas ......"))

    if Eleccion==1:
        n=fun.Entrada()
        fun.Primo(n)
    if Eleccion==2:
        n=fun.Entrada()
        fun.Multiplicar(n)
    if Eleccion==3:
        n=fun.Entrada()
        fun.Fibonacci(n)
    if Eleccion==4:
        fun.Lista()
    if Eleccion==5:
        fun.Maximo()
    if Eleccion==6:
        n=fun.Entrada()
        fun.PrimoEnesimo(n)
    elif Eleccion==0:
        Salir = False
    else:
        print("digita un numero de la lista")
print("/////*************************************************************")
print("gracia te esperamos ")
print("/////*************************************************************")
