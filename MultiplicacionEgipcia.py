#Estecambioesopcional
valoresCol1 = []
valoresCol2 = []
A = []

def imprimir(resultado):
    print("|Columna 1\t|Columna 2\t|")
    for i in range(len(valoresCol1)):
        print("|\t" + str(valoresCol2[i]) + "\t|\t" + str(valoresCol1[i]) + "\t|", end=" ")
        if str(i) in A : print("<----") 
        else: print(" ")

    print("\nSe suman:", end=" ")
    for i in range(len(A)):
        print(valoresCol2[int(A[i])], end=" ")
        if(i < len(A)-1): print(" + ", end=" ")
        else: print(" = ", end=" ")

    print(resultado)
        
def multiplicacion(num1, num2):
    global valoresCol1, valoresCol2, A  # Indicar que se usarán las variables globales
    
    valoresCol1.clear()  # Limpiar los arreglos antes de usarlos nuevamente
    valoresCol2.clear()
    A.clear()

    i = 1
    mulResultado = 0

    # Generar columnas con valores para el algoritmo de multiplicación
    while i <= num2:
        valoresCol1.append(i)
        valoresCol2.append(num1)
        i = i * 2
        num1 = num1 * 2

    resultado = []
    n = len(valoresCol1)

    # Generar todos los posibles subconjuntos de valoresCol1 y encontrar aquellos con suma igual a num2
    for i in range(1 << n):
        suma_actual = sum(valoresCol1[j] for j in range(n) if (i & (1 << j)) != 0)

        if suma_actual == num2:
            resultado.append([j for j in range(n) if (i & (1 << j)) != 0])

    # Convertir resultado a cadena y luego a una lista de índices
    cadena = str(resultado[0])
    cadena2 = cadena.replace("[", "").replace("]", "")
    A.extend(cadena2.split(", "))  # Usar extend para actualizar la variable global


    # Realizar la multiplicación acumulada de valoresCol2 utilizando los índices obtenidos
    for i in range(len(A)):
        mulResultado += valoresCol2[int(A[i])]

    return mulResultado    

if __name__ == '__main__':
    num1 = int(input("Ingrese el primer valor a multiplicar: "))
    num2 = int(input("Ingrese el segundo valor a multiplicar: "))
        
    # Llamar a la función multiplicacion y mostrar el resultado
    imprimir(multiplicacion(num1, num2))


