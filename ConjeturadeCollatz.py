def conjetura_collatz():
    n = int(input("Ingrese un numero entero: ")) #Input int
    iteraciones = 0
    while n != 1:       #Termina en n == 1
        iteraciones +=1
        if n % 2 == 0:
            print(str(n) + "\tEs par")
            n = n // 2 # Si es par, divide de forma entera
        else:
            print(str(n) + "\tEs impar")
            n = 3 * n + 1 #Impar, multiplica por 3 y suma 1
    print(str(n) + "\tValor final")     #Imprime 1, al terminar el algoritmo       
    print("Con " + str(iteraciones) + " Iteraciones")

if __name__ == '__main__':
    conjetura_collatz()