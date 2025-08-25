# ACTIVIDAD 1
def actividad_1():
    """
    Solicita la edad del usuario y, si es mayor de 18 años, muestra:
    "Es mayor de edad".
    """
    edad = int(input("Ingresa tu edad: "))
    if edad > 18:
        print("Es mayor de edad")
    else:
        print("No es mayor de 18 años")


# ACTIVIDAD 2
def actividad_2():
    """
    Solicita la nota del usuario. Si es mayor o igual a 6 => "Aprobado",
    en caso contrario => "Desaprobado".
    """
    nota = float(input("Ingresa tu nota (0-10): "))
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")


# ACTIVIDAD 3
def actividad_3():
    """
    Permite ingresar solo números pares:
    - Si el número es par: "Ha ingresado un número par".
    - Si no: "Por favor, ingrese un número par".
    """
    numero = int(input("Ingresa un número: "))
    if numero % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")


# ACTIVIDAD 4
def actividad_4():
    """
    Solicita la edad y clasifica al usuario en categorías:
    - Niño/a: < 12
    - Adolescente: 12 <= edad < 18
    - Adulto/a joven: 18 <= edad < 30
    - Adulto/a: >= 30
    """
    edad = int(input("Ingresa tu edad: "))
    if edad < 12:
        print("Niño/a")
    elif 12 <= edad < 18:
        print("Adolescente")
    elif 18 <= edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")


# ACTIVIDAD 5
def actividad_5():
    """
    Permite introducir contraseñas de entre 8 y 14 caracteres (incluidos).
    - Longitud adecuada: "Ha ingresado una contraseña correcta"
    - En otro caso: "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"
    """
    password = input("Ingresa una contraseña: ")
    if 8 <= len(password) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# ACTIVIDAD 6
def actividad_6():
    """
    Genera una lista de 50 números aleatorios entre 1 y 100, calcula
    moda, mediana y media; luego determina el sesgo según el criterio:
    - Sesgo positivo (derecha): media > mediana > moda
    - Sesgo negativo (izquierda): media < mediana < moda
    - Sin sesgo: media == mediana == moda
    (Si no cumple estrictamente, informa que no se puede determinar con este criterio.)
    """
    import random
    from statistics import mean, median, mode, StatisticsError
    try:
        from statistics import multimode  # Python 3.8+
    except ImportError:
        multimode = None  # No debería ocurrir en versiones actuales

    numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
    la_media = mean(numeros_aleatorios)
    la_mediana = median(numeros_aleatorios)
    try:
        la_moda = mode(numeros_aleatorios)
    except StatisticsError:
        # Lista multimodal: tomamos la primera moda como referencia
        if multimode is not None:
            la_moda = multimode(numeros_aleatorios)[0]
        else:
            # Reimplementación simple de "primera moda"
            from collections import Counter
            conteo = Counter(numeros_aleatorios).most_common()
            la_moda = conteo[0][0]

    print(f"Números: {numeros_aleatorios}")
    print(f"Media:   {la_media:.2f}")
    print(f"Mediana: {la_mediana:.2f}")
    print(f"Moda:    {la_moda}")

    if la_media > la_mediana > la_moda:
        print("Resultado: Sesgo positivo (a la derecha).")
    elif la_media < la_mediana < la_moda:
        print("Resultado: Sesgo negativo (a la izquierda).")
    elif la_media == la_mediana == la_moda:
        print("Resultado: Sin sesgo.")
    else:
        print("Resultado: No se puede determinar el sesgo con este criterio (no cumple estrictamente).")


# ACTIVIDAD 7
def actividad_7():
    """
    Solicita una frase o palabra. Si termina con vocal, añade '!' al final;
    en caso contrario, deja el string sin cambios.
    Considera vocales con y sin tilde (mayúsculas/minúsculas).
    """
    texto = input("Ingresa una palabra o frase: ")
    texto_sin_espacios_finales = texto.rstrip()
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    if texto_sin_espacios_finales and texto_sin_espacios_finales[-1] in vocales:
        print(texto_sin_espacios_finales + "!")
    else:
        print(texto)


# ACTIVIDAD 8
def actividad_8():
    """
    Pide el nombre y una opción (1/2/3):
    1) Mayúsculas (upper)
    2) Minúsculas (lower)
    3) Primera letra mayúscula (title)
    """
    nombre = input("Ingresa tu nombre: ")
    opcion = input("Elige opción (1: mayúsculas, 2: minúsculas, 3: primera letra mayúscula): ")

    if opcion == "1":
        print(nombre.upper())
    elif opcion == "2":
        print(nombre.lower())
    elif opcion == "3":
        print(nombre.title())
    else:
        print("Opción inválida. Debe ser 1, 2 o 3.")


# ACTIVIDAD 9
def actividad_9():
    """
    Solicita la magnitud de un terremoto y clasifica según la escala indicada:
    - < 3: "Muy leve" (imperceptible)
    - 3 <= x < 4: "Leve"
    - 4 <= x < 5: "Moderado"
    - 5 <= x < 6: "Fuerte"
    - 6 <= x < 7: "Muy Fuerte"
    - >= 7: "Extremo"
    """
    magnitud = float(input("Ingresa la magnitud del terremoto (escala de Richter): "))

    if magnitud < 3:
        print("Muy leve (imperceptible)")
    elif 3 <= magnitud < 4:
        print("Leve (ligeramente perceptible)")
    elif 4 <= magnitud < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños)")
    elif 5 <= magnitud < 6:
        print("Fuerte (puede causar daños en estructuras débiles)")
    elif 6 <= magnitud < 7:
        print("Muy Fuerte (puede causar daños significativos)")
    else:
        print("Extremo (puede causar graves daños a gran escala)")


# ACTIVIDAD 10
def actividad_10():
    """
    Pregunta hemisferio (N/S), mes (1-12) y día (1-31), e informa la estación
    correspondiente según la tabla provista.
    """
    hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").strip().upper()
    mes = int(input("Ingresa el mes (1-12): "))
    dia = int(input("Ingresa el día (1-31): "))

    def en_rango(m_d, inicio, fin):
        """
        Devuelve True si la fecha (mes, día) está entre 'inicio' y 'fin' (ambos inclusive).
        Soporta rangos que cruzan el fin de año (ej.: 21/12 a 20/03).
        """
        m, d = m_d
        mi, di = inicio
        mf, df = fin

        if (mi, di) <= (mf, df):
            return (mi, di) <= (m, d) <= (mf, df)
        else:
            # Rango que pasa por fin de año: (inicio -> 31/12) o (01/01 -> fin)
            return (m, d) >= (mi, di) or (m, d) <= (mf, df)

    fecha = (mes, dia)

    # Estaciones del HEMISFERIO NORTE (tabla)
    INVIERNO_N = ((12, 21), (3, 20))
    PRIMAVERA_N = ((3, 21), (6, 20))
    VERANO_N = ((6, 21), (9, 20))
    OTONO_N = ((9, 21), (12, 20))

    if hemisferio not in ("N", "S"):
        print("Entrada inválida para hemisferio. Debe ser 'N' o 'S'.")
        return

    if en_rango(fecha, *INVIERNO_N):
        estacion_norte = "Invierno"
    elif en_rango(fecha, *PRIMAVERA_N):
        estacion_norte = "Primavera"
    elif en_rango(fecha, *VERANO_N):
        estacion_norte = "Verano"
    elif en_rango(fecha, *OTONO_N):
        estacion_norte = "Otoño"
    else:
        estacion_norte = "Desconocida"

    if hemisferio == "N":
        print(f"Estación: {estacion_norte}")
    else:
        # En el hemisferio sur las estaciones son opuestas a las del norte
        equivalencias_sur = {
            "Invierno": "Verano",
            "Primavera": "Otoño",
            "Verano": "Invierno",
            "Otoño": "Primavera",
        }
        estacion_sur = equivalencias_sur.get(estacion_norte, "Desconocida")
        print(f"Estación: {estacion_sur}")


# Menú opcional para facilitar pruebas desde consola. 
if __name__ == "__main__":
 
    print("TP 3 - Estructuras condicionales (Menú de prueba)")
    print("1) Actividad 1")
    print("2) Actividad 2")
    print("3) Actividad 3")
    print("4) Actividad 4")
    print("5) Actividad 5")
    print("6) Actividad 6")
    print("7) Actividad 7")
    print("8) Actividad 8")
    print("9) Actividad 9")
    print("10) Actividad 10")
    print("0) Salir")

    try:
        opcion = int(input("Selecciona una opción: "))
    except ValueError:
        print("Opción inválida.")
        exit(0)

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
        10: actividad_10
    }
    if opcion == 0:
        print("Fin del programa.")
    else:
        func = funciones.get(opcion)
        if func is None:
            print("Opción inválida.")
        else:
            func()
