
def digitoCuatro(n):
    if n% 10 == 4:
        print("El número finaliza en cuatro")
        return True
    else:
        print("El número no finaliza en cuatro")
        return False

N = int(input("Ingrese un número: "))
digitoCuatro(N)

