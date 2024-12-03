import random

def cargar_notas(participantes):
    matriz = [[0] * 4 for _ in range(participantes)]  # Crear matriz vacía

    for i in range(participantes):
        matriz[i][0] = i + 1  # Número de participante autoincremental
        print(f"Ingresando datos para el participante {i + 1}:")
        for j in range(3):
            nota_valida = False
            while not nota_valida:
                entrada = input(f"Ingrese la nota del jurado {j + 1} (1-100): ")
                if entrada.isdigit():  # Verificar si la entrada es un número
                    nota = int(entrada)
                    if 1 <= nota <= 100:  # Validar rango
                        matriz[i][j + 1] = nota
                        nota_valida = True
                    else:
                        print("La nota debe estar entre 1 y 100.")
                else:
                    print("Por favor, ingrese un número válido.")
    return matriz
def calcular_promedio(fila):
    total = 0
    for nota in fila[1:]:
        total += nota
    return total / 3

def calcular_suma(fila):
    total = 0
    for nota in fila[1:]:
        total += nota
    return total

def mostrar_votos(matriz):
    print(f"{'Participante':<15}{'Jurado 1':<10}{'Jurado 2':<10}{'Jurado 3':<10}{'Promedio':<10}")
    for fila in matriz:
        promedio = calcular_promedio(fila)
        print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}{promedio:<10.2f}")

def ordenar_por_promedio(matriz, orden):
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            prom_i = calcular_promedio(matriz[i])
            prom_j = calcular_promedio(matriz[j])
            if (orden == "ascendente" and prom_i > prom_j) or (orden == "descendente" and prom_i < prom_j):
                matriz[i], matriz[j] = matriz[j], matriz[i]

def peores_tres(matriz):
    copia = [fila[:] for fila in matriz]
    ordenar_por_promedio(copia, "ascendente")
    print("Peores 3 participantes:")
    mostrar_votos(copia[:3])

def mayores_promedio(matriz):
    total_promedio = 0
    cantidad_notas = 0
    for fila in matriz:
        for nota in fila[1:]:
            total_promedio += nota
            cantidad_notas += 1
    promedio_general = total_promedio / cantidad_notas

    print(f"Promedio total: {promedio_general:.2f}")
    print("Participantes con promedio mayor al total:")
    for fila in matriz:
        promedio = calcular_promedio(fila)
        if promedio > promedio_general:
            print(f"Participante {fila[0]} con promedio {promedio:.2f}")

def jurado_malo(matriz):
    promedios_jurados = [0, 0, 0]  # Lista para almacenar los promedios de los tres jurados
    cantidad_participantes = len(matriz)

    # Calcular el promedio de cada jurado manualmente
    for i in range(3):
        total = 0
        for fila in matriz:
            total += fila[i + 1]  # Sumar las notas del jurado correspondiente
        promedios_jurados[i] = total / cantidad_participantes

    # Encontrar el jurado con el peor promedio manualmente
    peor_promedio = promedios_jurados[0]
    indice_peor = 0
    for i in range(1, 3):  # Recorremos los índices 1 y 2
        if promedios_jurados[i] < peor_promedio:
            peor_promedio = promedios_jurados[i]
            indice_peor = i

    # Mostrar el jurado con el peor promedio
    print(f"El jurado {indice_peor + 1} tiene el peor promedio: {peor_promedio:.2f}")

def sumatoria(matriz):
    objetivo_valido = False
    while not objetivo_valido:
        entrada = input("Ingrese un número entre 3 y 300: ")
        if entrada.isdigit():
            objetivo = int(entrada)
            if 3 <= objetivo <= 300:
                objetivo_valido = True
            else:
                print("El número debe estar entre 3 y 300.")
        else:
            print("Por favor, ingrese un número válido.")
    
    encontrados = []
    for fila in matriz:
        suma_notas = calcular_suma(fila)
        if suma_notas == objetivo:
            encontrados += [fila]  # Evita usar append
    if len(encontrados) > 0:
        print("Participantes con suma igual al objetivo:")
        mostrar_votos(encontrados)
    else:
        print("No se encontraron participantes con esa suma.")

def definir_ganador(matriz):
    ganadores = []
    max_promedio = calcular_promedio(matriz[0])

    # Encontrar el promedio máximo manualmente
    for fila in matriz:
        promedio = calcular_promedio(fila)
        if promedio > max_promedio:
            max_promedio = promedio

    # Buscar los participantes con ese promedio máximo
    for fila in matriz:
        if calcular_promedio(fila) == max_promedio:
            ganadores += [fila]  # Evita usar append

    if len(ganadores) == 1:
        print(f"El ganador es el participante {ganadores[0][0]} con promedio {max_promedio:.2f}")
    else:
        print("Desempate necesario entre los siguientes participantes:")
        for ganador in ganadores:
            print(f"Participante {ganador[0]} con promedio {max_promedio:.2f}")

        votos_desempate = [0] * len(ganadores)
        for _ in range(3):  # Simulamos los votos de los jurados
            eleccion = random.randint(1, len(ganadores))  # Número aleatorio
            votos_desempate[eleccion - 1] += 1

        # Encontrar el índice del ganador final
        max_votos = votos_desempate[0]
        indice_ganador = 0
        for i in range(1, len(votos_desempate)):
            if votos_desempate[i] > max_votos:
                max_votos = votos_desempate[i]
                indice_ganador = i

        ganador_final = ganadores[indice_ganador]
        print(f"El ganador final es el participante {ganador_final[0]}")

