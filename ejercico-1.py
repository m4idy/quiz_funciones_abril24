def tabla_multiplicar(n):
    print("tabla del " + str(N))
    for i in range(1,11):
        solucion=N*i
        print(N, "X", i, "=", solucion)

N=int(input("ingrese el numero que desea ver la tabla: "))
tabla_multiplicar(N)

