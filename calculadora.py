# calculator.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida"

def calculadora():
    print("Bienvenido a la calculadora")
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    operacion = input("Seleccione una operación (1/2/3/4): ")

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if operacion == '1':
        print("Resultado:", suma(num1, num2))
    elif operacion == '2':
        print("Resultado:", resta(num1, num2))
    elif operacion == '3':
        print("Resultado:", multiplicacion(num1, num2))
    elif operacion == '4':
        print("Resultado:", division(num1, num2))
    else:
        print("Operación no válida")

if __name__ == "__main__":
    calculadora()
