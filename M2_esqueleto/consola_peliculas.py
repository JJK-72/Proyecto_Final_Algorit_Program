
import modulo_peliculas as mod

def mostrar_informacion_pelicula(pelicula: dict) -> None:
    print("Nombre: " + pelicula["nombre"])
    print("Año: " + str(pelicula["anio"]))
    print("Duración: " + str(pelicula["duracion"]) + " mins")
    print("Género: " + pelicula["genero"])
    print("Clasificación: " + pelicula["clasificacion"])
    hora = pelicula["hora"]
    dia = pelicula["dia"]
    print("Día: " + dia + " Hora: " + str(hora // 100).zfill(2) + ":" + str(hora % 100).zfill(2))

def ejecutar_encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    pelicula_larga = mod.encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    if pelicula_larga:
        mostrar_informacion_pelicula(pelicula_larga)
    else:
        print("No hay películas en la lista.")

def ejecutar_consultar_duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    promedio = mod.duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    print("La duración promedio de las películas es: " + promedio)

def ejecutar_encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    anio = input("Ingrese el año: ")
    estrenos = mod.encontrar_estrenos(p1, p2, p3, p4, p5, int(anio))
    if estrenos == "":
        print("No hay estrenos después de ese año.")
    else:
        print("Películas estrenadas después de " + anio + ": " + estrenos)

def ejecutar_cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    cantidad = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
    print("Número de películas con clasificación 18+: " + str(cantidad))

def ejecutar_reagendar_pelicula(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    nombre = input("Ingrese el nombre de la película que desea reagendar: ")
    pelicula = mod.encontrar_pelicula(nombre, p1, p2, p3, p4, p5)
    
    if pelicula == None:
        print("No hay ninguna película con este nombre.")
        return

    nueva_hora = int(input("Ingrese la nueva hora (HHMM): "))
    nuevo_dia = input("Ingrese el nuevo día: ")
    control_horario_input = input("¿Desea controlar las preferencias de horario? (s/n): ")
    if control_horario_input == 's':
        control_horario = True
    else:
        control_horario = False

    if mod.reagendar_pelicula(pelicula, nueva_hora, nuevo_dia, control_horario, p1, p2, p3, p4, p5):
        print("Película reagendada exitosamente.")
    else:
        print("No se pudo reagendar la película.")

def ejecutar_decidir_invitar(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    nombre = input("Ingrese el nombre de la película: ")
    pelicula = mod.encontrar_pelicula(nombre, p1, p2, p3, p4, p5)
    
    if pelicula == None:
        print("No hay ninguna película con este nombre.")
        return

    edad = int(input("¿Cuál es la edad del invitado? "))
    autorizacion = input("¿Tiene autorización de los padres? (s/n): ")
    
    if autorizacion == 's':
        autorizacion_padres = True
    else:
        autorizacion_padres = False

    if mod.decidir_invitar(pelicula, edad, autorizacion_padres):
        print("Se puede invitar a la persona.")
    else:
        print("No se puede invitar a la persona.")

def iniciar_aplicacion():
    pelicula1 = mod.crear_pelicula("Toy Story", "Familiar, Comedia", 81, 1995, "7+", 1000, "Domingo")
    pelicula2 = mod.crear_pelicula("Parasite", "Thriller, Comedia", 132, 2019, "18+", 1400, "Domingo")  
    pelicula3 = mod.crear_pelicula("Avengers: Endgame", "Ciencia Ficción, Acción", 181, 2019, "13+", 1630, "Sábado")
    pelicula4 = mod.crear_pelicula("The Lion King", "Familiar, Comedia", 88, 1994, "Todos", 1800, "Jueves")
    pelicula5 = mod.crear_pelicula("The Shawshank Redemption", "Drama", 142, 1994, "16+", 2000, "Lunes")   
    
    ejecutando = True
    while ejecutando:            
        print("\n\nMi agenda de películas para la semana de receso" +"\n"+("-"*50))
        print("Película 1")
        mostrar_informacion_pelicula(pelicula1)
        print("-"*50)
        
        print("Película 2")
        mostrar_informacion_pelicula(pelicula2)
        print("-"*50)
        
        print("Película 3")
        mostrar_informacion_pelicula(pelicula3)
        print("-"*50)
        
        print("Película 4")
        mostrar_informacion_pelicula(pelicula4)
        print("-"*50)
        
        print("Película 5")
        mostrar_informacion_pelicula(pelicula5)
        print("-"*50)
        
        ejecutando = mostrar_menu_aplicacion(pelicula1, pelicula2, pelicula3, pelicula4, pelicula5)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")

def mostrar_menu_aplicacion(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> bool:
    print("Menú de opciones")
    print(" 1 - Consultar película más larga")
    print(" 2 - Consultar duración promedio de las películas")
    print(" 3 - Consultar películas de estreno")
    print(" 4 - Consultar cuántas películas tienen clasificación 18+")
    print(" 5 - Reagendar película")
    print(" 6 - Verificar si se puede invitar a alguien")    
    print(" 7 - Salir de la aplicación")

    opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()
    
    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    elif opcion_elegida == "2":
        ejecutar_consultar_duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    elif opcion_elegida == "3":
        ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5)
    elif opcion_elegida == "4":
        ejecutar_cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)        
    elif opcion_elegida == "5":
        ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5) 
    elif opcion_elegida == "6":
        ejecutar_decidir_invitar(p1, p2, p3, p4, p5) 
    elif opcion_elegida == "7":
        continuar_ejecutando = False
    else:
        print("La opción " + opcion_elegida + " no es una opción válida.")
    
    return continuar_ejecutando

iniciar_aplicacion()

