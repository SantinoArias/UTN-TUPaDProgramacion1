from random import randint

# ---------------------------------------------------------------------------
# Utilidades de entrada 
# ---------------------------------------------------------------------------

def leer_entero(mensaje: str) -> int:
    """
    Solicita un entero por consola con manejo de errores.
    Repite el pedido hasta que el usuario ingrese un valor válido.
    """
    while True:
        dato = input(mensaje)
        try:
            return int(dato)
        except ValueError:
            print("Entrada inválida: debe ser un número entero.")

def leer_entero_positivo(mensaje: str, incluir_cero: bool = True) -> int:
    """
    Solicita un entero positivo (o no-negativo si incluir_cero=True).
    """
    while True:
        n = leer_entero(mensaje)
        if incluir_cero and n >= 0:
            return n
        if (not incluir_cero) and n > 0:
            return n
        print("Entrada inválida: debe ser un entero positivo." if not incluir_cero
              else "Entrada inválida: debe ser un entero mayor o igual a 0.")

# Cantidad de entradas para las actividades 8 y 9.
CANTIDAD_ENTRADAS = 10

# ---------------------------------------------------------------------------
# ACTIVIDAD 1
# ---------------------------------------------------------------------------

def actividad_1():
    """
    Imprime todos los enteros desde 0 hasta 100 (inclusives), uno por línea,
    en orden creciente.
    """
    for i in range(0, 101):
        print(i)

# ---------------------------------------------------------------------------
# ACTIVIDAD 2
# ---------------------------------------------------------------------------

def actividad_2():
    """
    Solicita un entero y muestra la cantidad de dígitos que contiene.
    Considera el valor absoluto (el signo '-' no cuenta como dígito).
    Caso especial: 0 tiene 1 dígito.
    """
    n = leer_entero("Ingresá un número entero: ")
    n_abs = abs(n)
    if n_abs == 0:
        cantidad = 1
    else:
        cantidad = 0
        while n_abs > 0:
            n_abs //= 10
            cantidad += 1
    print(f"Cantidad de dígitos: {cantidad}")

# ---------------------------------------------------------------------------
# ACTIVIDAD 3
# ---------------------------------------------------------------------------

def actividad_3():
    """
    Solicita dos enteros y suma todos los enteros estrictamente comprendidos
    entre ambos (excluye los extremos).
    """
    a = leer_entero("Ingresá el primer entero: ")
    b = leer_entero("Ingresá el segundo entero: ")
    inicio = min(a, b) + 1
    fin = max(a, b)
    acumulado = 0
    for x in range(inicio, fin):
        acumulado += x
    print(f"Suma entre {a} y {b} (excluyendo extremos): {acumulado}")

# ---------------------------------------------------------------------------
# ACTIVIDAD 4
# ---------------------------------------------------------------------------

def actividad_4():
    """
    Permite ingresar enteros en secuencia y los suma.
    El programa se detiene y muestra el total cuando el usuario ingresa 0.
    """
    total = 0
    while True:
        n = leer_entero("Ingresá un entero (0 para terminar): ")
        if n == 0:
            break
        total += n
    print(f"Total acumulado: {total}")

# ---------------------------------------------------------------------------
# ACTIVIDAD 5
# ---------------------------------------------------------------------------

def actividad_5():
    """
    Juego de adivinanza:
    - La computadora "piensa" un número aleatorio entre 0 y 9.
    - El usuario intenta adivinarlo.
    - Al finalizar, muestra la cantidad de intentos necesarios.
    """
    secreto = randint(0, 9)
    intentos = 0
    while True:
        guess = leer_entero("Adiviná el número (0 a 9): ")
        intentos += 1
        if guess == secreto:
            print(f"¡Correcto! El número era {secreto}. Intentos: {intentos}")
            break
        else:
            # Pista opcional (podés comentar las siguientes 2 líneas si no querés pistas)
            print("Más chico..." if guess > secreto else "Más grande...")

# ---------------------------------------------------------------------------
# ACTIVIDAD 6
# ---------------------------------------------------------------------------

def actividad_6():
    """
    Imprime todos los números pares entre 0 y 100 (inclusive),
    en orden decreciente.
    """
    for i in range(100, -1, -2):
        print(i)

# ---------------------------------------------------------------------------
# ACTIVIDAD 7
# ---------------------------------------------------------------------------

def actividad_7():
    """
    Solicita un entero positivo N y calcula la suma de todos los enteros
    comprendidos entre 0 y N, incluyendo ambos extremos (0 + 1 + ... + N).
    """
    n = leer_entero_positivo("Ingresá un entero positivo N: ", incluir_cero=True)
    total = 0
    for x in range(0, n + 1):
        total += x
    print(f"Suma 0..{n}: {total}")

# ---------------------------------------------------------------------------
# ACTIVIDAD 8
# ---------------------------------------------------------------------------

def actividad_8():
    """
    Permite ingresar CANTIDAD_ENTRADAS números enteros y luego informa:
      - Cuántos son pares
      - Cuántos son impares
      - Cuántos son negativos
      - Cuántos son positivos
    Nota: 0 cuenta como par, pero no es positivo ni negativo.
    """
    pares = impares = negativos = positivos = 0
    print(f"Ingresá {CANTIDAD_ENTRADAS} números enteros:")
    for _ in range(CANTIDAD_ENTRADAS):
        n = leer_entero("  > ")
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
        if n > 0:
            positivos += 1
        elif n < 0:
            negativos += 1
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")
    print(f"Positivos: {positivos}")
    print(f"Negativos: {negativos}")

# ---------------------------------------------------------------------------
# ACTIVIDAD 9
# ---------------------------------------------------------------------------

def actividad_9():
    """
    Permite ingresar CANTIDAD_ENTRADAS números enteros y calcula la media
    (promedio aritmético) de esos valores.
    """
    suma = 0
    print(f"Ingresá {CANTIDAD_ENTRADAS} números enteros:")
    for _ in range(CANTIDAD_ENTRADAS):
        n = leer_entero("  > ")
        suma += n
    media = suma / CANTIDAD_ENTRADAS
    print(f"Media: {media}")

# ---------------------------------------------------------------------------
# ACTIVIDAD 10
# ---------------------------------------------------------------------------

def actividad_10():
    """
    Invierte el orden de los dígitos de un número entero ingresado por el usuario.
    Ejemplo: 547 -> 745. Mantiene el signo si es negativo (ej.: -123 -> -321).
    Implementado con aritmética (while) para ejercitar bucles.
    """
    n = leer_entero("Ingresá un entero: ")

    signo = -1 if n < 0 else 1
    n_abs = abs(n)
    invertido = 0

    if n_abs == 0:
        invertido = 0
    else:
        while n_abs > 0:
            ultimo = n_abs % 10
            invertido = invertido * 10 + ultimo
            n_abs //= 10

    resultado = signo * invertido
    print(f"Número invertido: {resultado}")

# ---------------------------------------------------------------------------
# Menú de prueba 
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("TP - Estructuras repetitivas (Menú de prueba)")
    print("1) Imprimir 0..100")
    print("2) Contar dígitos de un entero")
    print("3) Suma entre dos enteros (excluye extremos)")
    print("4) Suma en secuencia hasta 0")
    print("5) Juego de adivinar (0..9)")
    print("6) Pares 100..0 decreciente")
    print("7) Suma 0..N")
    print("8) Contadores (pares/impares/neg/pos) sobre N entradas")
    print("9) Media aritmética sobre N entradas")
    print("10) Invertir dígitos")
    print("0) Salir")

    funciones = {
        1: actividad_1,
        2: actividad_2,
        3: actividad_3,
        4: actividad_4,
        5: actividad_5,
        6: actividad_6,
        7: actividad_7,
        8: actividad_8,
        9: actividad_9,
        10: actividad_10,
    }

    while True:
        try:
            opcion = int(input("Seleccioná una opción: "))
        except ValueError:
            print("Opción inválida.")
            continue

        if opcion == 0:
            print("Fin del programa.")
            break

        func = funciones.get(opcion)
        if func is None:
            print("Opción inválida.")
        else:
            print("-" * 50)
            func()
            print("-" * 50)
