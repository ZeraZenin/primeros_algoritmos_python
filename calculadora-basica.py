numero1 = float(input("Escribe el primer número: "))
numero2 = float(input("Escribe el segundo número:"))
operacion = input("Escribe la operación (+, -, *, /):")
if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "*":
    resultado = numero1 *numero2
elif operacion == "/":
    resultado = numero1 / numero2
else:
    resultado = "Operación no válida"
print("Resultado:", resultado)