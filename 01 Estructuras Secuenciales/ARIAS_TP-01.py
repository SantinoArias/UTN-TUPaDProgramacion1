
# ACTIVIDAD 1
def actividad_1():
    # Crear un programa que imprima “Hola Mundo!”
    print("Hola Mundo!")


# ACTIVIDAD 2
def actividad_2():
    # Pedir al usuario su nombre e imprimir "Hola [nombre]!"
    nombre = input("Por favor, ingresa tu nombre: ")
    print(f"Hola {nombre}!")


# ACTIVIDAD 3
def actividad_3():
    # Pedir nombre, apellido, edad y lugar, e imprimir una presentación completa.
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")
    lugar = input("Ingresa tu lugar de residencia: ")
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")


# ACTIVIDAD 4
def actividad_4():
    # Pedir el radio de un círculo y mostrar su área y perímetro.
    radio = float(input("Ingresa el radio del círculo: "))
    area = 3.14159 * (radio ** 2)
    perimetro = 2 * 3.14159 * radio
    print(f"El área del círculo es: {area} y el perímetro es: {perimetro}")


# ACTIVIDAD 5
def actividad_5():
    # Pedir una cantidad de segundos y mostrar a cuántas horas equivale.
    segundos = int(input("Ingresa una cantidad de segundos: "))
    horas = segundos // 3600
    print(f"{segundos} segundos equivalen a {horas} horas.")

# ACTIVIDAD 6
def actividad_6():
    # Pedir un número e imprimir su tabla de multiplicar.
    numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
    print(f"La tabla de multiplicar del {numero} es:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    
# ACTIVIDAD 7
def actividad_7():
    # Pedir dos números y mostrar suma, resta, multiplicación y división.
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2 if num2 != 0 else "Indefinido (división por cero)"
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")


# ACTIVIDAD 8
def actividad_8():
    # Pedir altura y peso, e imprimir el índice de masa corporal (IMC).
    altura = float(input("Ingresa tu altura en metros: "))
    peso = float(input("Ingresa tu peso en kilogramos: "))
    imc = peso / (altura ** 2)
    print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")
    


# ACTIVIDAD 9
def actividad_9():
    # Pedir temperatura en Celsius y mostrarla en Fahrenheit.
    celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}°F")


# ACTIVIDAD 10
def actividad_10():
    # Pedir 3 números e imprimir el promedio.
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))
    promedio = (num1 + num2 + num3) / 3
    print(f"El promedio de los números es: {promedio:.2f}")


# Para probar una actividad, descomentar la función correspondiente:

# actividad_1()
# actividad_2()
# actividad_3()
# actividad_4()
# actividad_5()
# actividad_6()
# actividad_7()
# actividad_8()
# actividad_9()
# actividad_10()
