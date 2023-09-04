def multiplicacion_rusa(num1, num2):
    resultado = 0
    
    # Mientras el primer número sea mayor a cero
    while num1 > 0:
        # Si el primer número es impar, suma el valor del segundo número al resultado acumulado
        if num1 % 2 != 0:
            resultado += num2
        
        # Divide el primer número por 2 y duplica el segundo número
        num1 //= 2
        num2 *= 2
    
    return resultado

if __name__ == '__main__':
    # Solicita al usuario ingresar los números a multiplicar
    num1 = int(input("Ingrese el primer valor a multiplicar: "))
    num2 = int(input("Ingrese el segundo valor a multiplicar: "))
    
    # Calcula y muestra el resultado de la multiplicación rusa
    print("El resultado de la multiplicación rusa es:", multiplicacion_rusa(num1, num2))
