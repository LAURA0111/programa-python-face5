# Problema 5 - Control de horas trabajadas

# Matriz con los recursos y horas trabajadas de lunes a viernes
# [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]

matriz_horas = [
    ["Carlos", 8, 9, 8, 10, 9],
    ["Laura", 7, 8, 7, 8, 7],
    ["Andrés", 9, 10, 9, 8, 10],
    ["María", 6, 7, 8, 7, 6]
]

# Función para calcular el total de horas y clasificar la jornada

def calcular_horas(recurso):
    nombre = recurso[0]
    horas = recurso[1:]

    total_horas = sum(horas)

    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return nombre, total_horas, clasificacion


# Mostrar resultados
print("REPORTE DE HORAS SEMANALES\n")

for recurso in matriz_horas:
    nombre, total, clasificacion = calcular_horas(recurso)

    print("Recurso:", nombre)
    print("Total de horas trabajadas:", total)
    print("Clasificación:", clasificacion)
    print("-----------------------------")