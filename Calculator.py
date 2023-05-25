from sympy import symbols, integrate

# Función para calcular la integral definida
def calcular_integral(funcion, variable, limite_inferior, limite_superior):
    x = symbols(variable)
    integral = integrate(funcion, (x, limite_inferior, limite_superior))
    return integral

# Solicitar la función y los límites al usuario
funcion = input("Ingrese la función: ")
variable = input("Ingrese la variable de integración: ")
limite_inferior = float(input("Ingrese el límite inferior: "))
limite_superior = float(input("Ingrese el límite superior: "))

# Calcular la integral definida
resultado = calcular_integral(funcion, variable, limite_inferior, limite_superior)
print("Resultado:", resultado)
