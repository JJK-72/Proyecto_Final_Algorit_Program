"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, clasificacion: str, hora: int, dia: str) -> dict:
    
    pelicula = {
        "nombre": nombre,
        "genero": genero,
        "duracion": duracion,
        "anio": anio,
        "clasificacion": clasificacion,
        "hora": hora,
        "dia": dia
    }
    return pelicula

p1 = crear_pelicula("Toy Story", "Familiar, Comedia", 81, 1995, "7+", 1000, "Domingo" )
p2 = crear_pelicula("Parasite", "thriller, comedia", 132, 2019, "16+", 1400, "Dmingo" )
p3 = crear_pelicula("Avengers: Endgame", "Ciencia Ficción, Acción", 181, 2019, "13+", 1630, "Sábado" )
p4 = crear_pelicula("The Lion King", "Familiar, comedia", 88, 1994, "Todos", 1800, " Jueves" )
p5 = crear_pelicula("The Shawshank Redemption", "Drama", 142, 1994, "16+", 2000, "Lunes" )


def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:

    d = {p1['nombre']: p1, p2['nombre']: p2, p3['nombre']: p3, p4['nombre']: p4, p5['nombre']: p5}

    NP = input('Ingrese el nombre de la película: ')

    nombre_pelicula = NP

    for pelicula in [p1, p2, p3, p4, p5]:

        if pelicula["nombre"] == nombre_pelicula:
            return pelicula
        
    return None


def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    l=[p1['duracion'], p2['duracion'], p3['duracion'], p4['duracion'], p5['duracion']]

    peliculas=[p1,p2,p3,p4,p5]

    for pelicula in peliculas:
        if pelicula['duracion']==max(l):
            return pelicula


def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:

    l=[p1['duracion'], p2['duracion'], p3['duracion'], p4['duracion'], p5['duracion']]

    prom = (sum(l)/len(l))
    horas = int(prom//60)
    minutos = int(prom%60)

    return (f'{horas}:{minutos}')
    

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:

    peliculas = [p1, p2, p3, p4, p5]
    estrenos = []

    for pelicula in peliculas:
        if (pelicula['anio']) > anio:
            estrenos.append(pelicula['nombre'])

    if len(estrenos) == 0:  
            return "Ninguna"
    
    return estrenos

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:

    contador = 0

    if p1['clasificacion'] == '18+':
        contador = contador + 1
    if p2['clasificacion'] == '18+':
        contador = contador + 1
    if p3['clasificacion'] == '18+':
        contador = contador + 1
    if p4['clasificacion'] == '18+':
        contador = contador + 1
    if p5['clasificacion'] == '18+':
        contador = contador + 1

    return contador


def reagendar_pelicula(pelicula: dict, nueva_hora: int, nuevo_dia: str, control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> bool:

    peliculas = [p1, p2, p3, p4, p5]
    
    for p in peliculas:
        if p['nombre'] != pelicula['nombre']:
            if p['dia'] == nuevo_dia:
                if nueva_hora >= p['hora'] and nueva_hora < (p['hora'] + p['duracion']):
                    print("Conflicto con", p['nombre'])
                    return False
                if p['hora'] >= nueva_hora and p['hora'] < (nueva_hora + pelicula['duracion']):
                    print("Conflicto con", p['nombre'])
                    return False

    if control_horario == True:
        if "Documental" in pelicula['genero']:
            if nueva_hora >= 2200:
                print("No ver documentales después de las 10 PM")
                return False

        if "Drama" in pelicula['genero']:
            if nuevo_dia == "viernes":
                print("No dramas los viernes")
                return False

        if nuevo_dia in ["lunes", "martes", "miércoles", "jueves", "viernes"]:
            if nueva_hora >= 2300 or nueva_hora < 600:
                print("No ver películas entre semana tarde o muy temprano")
                return False

    pelicula['hora'] = nueva_hora
    pelicula['dia'] = nuevo_dia

    return True



def decidir_invitar(peli: dict, edad_invitado: int) -> bool:

    invitar = input("¿Deseas invitar a alguien? (si/no): ")

    if invitar == 'no':
        print("No se realizará la invitación.")
        return False

    if invitar == 'si':
        autorizacion_padres = input("¿Tienes autorización de los padres? (si/no): ")
        
        if edad_invitado >= 18:
            print("Puedes invitar a la persona.")
            return True

        if edad_invitado < 15 and "Terror" in peli['genero']:
            print("No puedes invitar a menores de 15 a ver películas de terror.")
            return False

        if edad_invitado <= 10 and "Familiar" not in peli['genero']:
            print("Solo puedes invitar a menores de 10 a películas familiares.")
            return False

        if peli['clasificacion'] == '18+':
            if autorizacion_padres == 'no':
                print("Necesitas autorización de los padres para invitar a ver películas 18+.")
                return False

        print("Puedes invitar a la persona.")
        return True

    print("Opción no válida.")
    return False




