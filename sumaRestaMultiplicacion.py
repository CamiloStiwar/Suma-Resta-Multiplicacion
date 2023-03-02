
def funcionSuma(n1,n2):
    suma = n1 + n2
    return suma

def funcionResta(n1,n2):
    resta = n1 - n2
    return resta

def funcionMultiplicacion(n1,n2):
    multiplicacion = n1 * n2
    return multiplicacion

number1 = int(input("Por favor ingrese el primer numero: "))
number2 = int(input("Por favor ingrese el segundo numero: "))

suma = funcionSuma(number1,number2)
resta = funcionResta(number1,number2)
multiplicacion = funcionMultiplicacion(number1,number2)

print("El resultado de la suma es ", suma)
print("El restultado de la resta es ", resta)
print("El resultado de la multiplicación es ", multiplicacion)