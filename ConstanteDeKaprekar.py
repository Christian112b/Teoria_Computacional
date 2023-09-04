def ordenar_digitos(numero, ascendente):
    # Convierte el número en una lista de dígitos y la ordena
    digitos = list(str(numero))
    digitos.sort()
    if not ascendente:
        digitos.reverse()
    # Convierte la lista de dígitos ordenados de nuevo en un número entero
    return int(''.join(digitos))

def constanteDeKaprekar(numero):
    iteraciones = 0
    # Verifica si el número tiene todos los dígitos iguales
    if len((set(str(numero)))) == 1:
        return "El numero debe de tener 4 digitos distintos"
    
    n = numero
    while n != 6174:
        iteraciones += 1
        # Ordena los dígitos en orden descendente y ascendente, luego resta el menor del mayor
        n1 = ordenar_digitos(n, False)
        n2 = ordenar_digitos(n, True)
        n = n1 - n2

    return n, iteraciones

if __name__ == '__main__':
    n = int(input("Ingrese un numero con 4 digitos: "))
    constante, iteraciones = constanteDeKaprekar(n)
    print("La constante de Kaprekar es: " + str(constante) + ", Con " + str(iteraciones) + " Iteraciones.")
