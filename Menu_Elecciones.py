from Funciones_Elecciones import *


def menu():
    participantes = 5
    matriz = [[0] * 4 for _ in range(participantes)]  # Matriz inicial vacía
    while True:
        print("\nMenú de opciones:")
        print("1. Cargar Notas")
        print("2. Mostrar Votos")
        print("3. Ordenar por Nota Promedio")
        print("4. Peores 3 Participantes")
        print("5. Participantes con Promedio Mayor al Total")
        print("6. Jurado Malo")
        print("7. Participantes por Sumatoria de Notas")
        print("8. Definir Ganador")
        print("9. Salir")
        
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                matriz = cargar_notas(participantes)
                print("Notas cargadas correctamente.")
            case "2":
                mostrar_votos(matriz)
            case "3":
                orden = input("Ingrese el orden (ascendente o descendente): ")
                if orden == "ascendente" or orden == "descendente":
                    ordenar_por_promedio(matriz, orden)
                    print("Matriz ordenada.")
                else:
                    print("Orden inválido.")
            case "4":
                peores_tres(matriz)
            case "5":
                mayores_promedio(matriz)
            case "6":
                jurado_malo(matriz)
            case "7":
                sumatoria(matriz)
            case "8":
                definir_ganador(matriz)
            case "9":
                break

menu()