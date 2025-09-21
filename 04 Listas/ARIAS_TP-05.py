
from random import randint

# =========================
# Funciones de entrada 
# =========================

def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except:
            print("Error: ingresá un número entero.")

def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except:
            print("Error: ingresá un número (puede tener decimales).")

def pedir_float_rango(mensaje, minimo, maximo):
    while True:
        x = pedir_float(mensaje)
        if minimo <= x <= maximo:
            return x
        print(f"Debe estar entre {minimo} y {maximo}.")

# =========================
# Actividades
# =========================

def actividad_1():
    # Lista de 10 notas, promedio, max y min
    notas = []
    print("Ingresá 10 notas (0..10):")
    for i in range(10):
        n = pedir_float_rango(f" Nota {i+1}: ", 0, 10)
        notas.append(n)

    print("Notas:")
    for n in notas:
        print(n)

    suma = 0
    mayor = notas[0]
    menor = notas[0]
    for n in notas:
        suma += n
        if n > mayor:
            mayor = n
        if n < menor:
            menor = n

    print(f"Promedio: {suma/len(notas):.2f}")
    print(f"Mayor: {mayor:.2f}")
    print(f"Menor: {menor:.2f}")

def actividad_2():
    # Cargar 5 productos, ordenar y eliminar uno
    productos = []
    print("Cargá 5 productos:")
    for i in range(5):
        p = input(f" Producto {i+1}: ").strip()
        productos.append(p)

    ordenados = sorted(productos)
    print("Productos ordenados:")
    for p in ordenados:
        print(p)

    borrar = input("Producto a eliminar (exacto): ").strip()
    if borrar in productos:
        productos.remove(borrar)
        print("Lista actualizada:")
        for p in productos:
            print(p)
    else:
        print("No se encontró, sin cambios.")

def actividad_3():
    # 15 enteros al azar (1..100), separar pares e impares y contar
    numeros = []
    for _ in range(15):
        numeros.append(randint(1, 100))

    pares = []
    impares = []
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)

    print("Cantidad de pares:", len(pares))
    print("Cantidad de impares:", len(impares))

def actividad_4():
    # Quitar repetidos manteniendo el orden
    n = pedir_entero("Cantidad de elementos: ")
    datos = []
    for i in range(n):
        datos.append(input(f" Valor {i+1}: "))

    sin_rep = []
    for x in datos:
        if x not in sin_rep:
            sin_rep.append(x)

    print("Sin repetidos:")
    for x in sin_rep:
        print(x)

def actividad_5():
    # Lista de 8 estudiantes, agregar o eliminar uno
    alumnos = []
    print("Ingresá 8 estudiantes:")
    for i in range(8):
        alumnos.append(input(f" Estudiante {i+1}: ").strip())

    op = input("¿Agregar (A) / Eliminar (E) / Nada (N)? ").strip().upper()
    if op == "A":
        nuevo = input("Nombre a agregar: ").strip()
        alumnos.append(nuevo)
    elif op == "E":
        victima = input("Nombre a eliminar (exacto): ").strip()
        if victima in alumnos:
            alumnos.remove(victima)
        else:
            print("No se encontró.")

    print("Lista final:")
    for a in alumnos:
        print(a)

def actividad_6():
    # Rotar lista de 7 enteros a la derecha
    v = []
    print("Ingresá 7 enteros:")
    for i in range(7):
        v.append(pedir_entero(f" n[{i}]: "))

    if len(v) > 0:
        rotada = [v[-1]]
        i = 0
        while i < len(v)-1:
            rotada.append(v[i])
            i += 1
    else:
        rotada = []

    print("Original:")
    for x in v:
        print(x)
    print("Rotada:")
    for x in rotada:
        print(x)

def actividad_7():
    # Matriz 7x2 (min, max) -> promedios y mayor amplitud
    temps = []
    print("Ingresá mínima y máxima de 7 días:")
    for d in range(7):
        tmin = pedir_float(f" Día {d+1} - mínima: ")
        tmax = pedir_float(f" Día {d+1} - máxima: ")
        while tmax < tmin:
            print("La máxima no puede ser menor a la mínima.")
            tmin = pedir_float(f" Día {d+1} - mínima: ")
            tmax = pedir_float(f" Día {d+1} - máxima: ")
        temps.append([tmin, tmax])

    print("Matriz min/max:")
    for fila in temps:
        print(fila[0], fila[1])

    suma_min = 0
    suma_max = 0
    mayor_amp = None
    dia_mayor = None

    i = 0
    while i < 7:
        tmin = temps[i][0]
        tmax = temps[i][1]
        suma_min += tmin
        suma_max += tmax
        amp = tmax - tmin
        if mayor_amp is None or amp > mayor_amp:
            mayor_amp = amp
            dia_mayor = i + 1
        i += 1

    print(f"Promedio mínimas: {suma_min/7:.2f}")
    print(f"Promedio máximas: {suma_max/7:.2f}")
    print(f"Mayor amplitud: {mayor_amp:.2f} (día {dia_mayor})")

def actividad_8():
    # Notas de 5 estudiantes en 3 materias: promedio por estudiante y por materia
    filas = 5
    cols = 3
    notas = []
    print("Notas (0..10) de 5 estudiantes x 3 materias:")
    for i in range(filas):
        fila = []
        for j in range(cols):
            fila.append(pedir_float_rango(f" Est {i+1} Materia {j+1}: ", 0, 10))
        notas.append(fila)

    print("Matriz de notas:")
    for fila in notas:
        linea = ""
        for x in fila:
            linea += f"{x}\t"
        print(linea.rstrip())

    print("Promedio por estudiante:")
    for i in range(filas):
        s = 0
        for j in range(cols):
            s += notas[i][j]
        print(f" Est {i+1}: {s/cols:.2f}")

    print("Promedio por materia:")
    for j in range(cols):
        s = 0
        for i in range(filas):
            s += notas[i][j]
        print(f" Mat {j+1}: {s/filas:.2f}")

def actividad_9():
    # Ta-Te-Ti básico 3x3, sin detectar ganador
    tablero = [['-' for _ in range(3)] for _ in range(3)]

    def mostrar():
        for fila in tablero:
            print(fila[0], fila[1], fila[2])

    turno = 'X'
    jugadas = 0
    mostrar()
    while jugadas < 9:
        print(f"Turno {turno}")
        f = pedir_entero(" Fila (1..3): ") - 1
        c = pedir_entero(" Columna (1..3): ") - 1
        if f<0 or f>2 or c<0 or c>2:
            print("Posición inválida.")
            continue
        if tablero[f][c] != '-':
            print("Ocupada.")
            continue
        tablero[f][c] = turno
        jugadas += 1
        mostrar()
        turno = 'O' if turno == 'X' else 'X'
    print("Fin del juego.")

def actividad_10():
    # Ventas 4x7: totales por producto, mejor día, producto más vendido
    prod = 4
    dias = 7
    ventas = []
    print("Ingresá ventas (4 productos x 7 días):")
    for i in range(prod):
        fila = []
        for j in range(dias):
            fila.append(pedir_float(f" Prod {i+1} Día {j+1}: "))
        ventas.append(fila)

    print("Matriz de ventas:")
    for fila in ventas:
        linea = ""
        for x in fila:
            linea += f"{x}\t"
        print(linea.rstrip())

    print("Totales por producto:")
    tot_prod = []
    for i in range(prod):
        s = 0
        for j in range(dias):
            s += ventas[i][j]
        tot_prod.append(s)
        print(f" Producto {i+1}: {s:.2f}")

    # Mejor día (suma por columna)
    mejor_total = None
    mejor_dia = None
    j = 0
    while j < dias:
        s = 0
        i = 0
        while i < prod:
            s += ventas[i][j]
            i += 1
        if mejor_total is None or s > mejor_total:
            mejor_total = s
            mejor_dia = j + 1
        j += 1
    print(f"Mejor día: Día {mejor_dia} (total {mejor_total:.2f})")

    # Producto más vendido
    mayor = None
    idx = None
    i = 0
    while i < prod:
        if mayor is None or tot_prod[i] > mayor:
            mayor = tot_prod[i]
            idx = i + 1
        i += 1
    print(f"Más vendido: Producto {idx} (total {mayor:.2f})")

# =========================
# Menú simple
# =========================

def main():
    while True:
        print("\nTP5 - LISTAS (MENÚ)")
        print("1) Notas (promedio, máx, mín)")
        print("2) Productos (ordenar y eliminar)")
        print("3) Aleatorios pares/impares")
        print("4) Quitar repetidos")
        print("5) Estudiantes (agregar/eliminar)")
        print("6) Rotar lista a la derecha")
        print("7) Temperaturas semanales")
        print("8) Notas 5x3 (promedios)")
        print("9) Ta-Te-Ti 3x3")
        print("10) Ventas 4x7")
        print("0) Salir")

        op = pedir_entero("Opción: ")
        if op == 0:
            print("Fin.")
            break
        elif op == 1:
            actividad_1()
        elif op == 2:
            actividad_2()
        elif op == 3:
            actividad_3()
        elif op == 4:
            actividad_4()
        elif op == 5:
            actividad_5()
        elif op == 6:
            actividad_6()
        elif op == 7:
            actividad_7()
        elif op == 8:
            actividad_8()
        elif op == 9:
            actividad_9()
        elif op == 10:
            actividad_10()
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
