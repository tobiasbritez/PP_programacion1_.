"""
Una empresa se dedica al almacenamiento y posterior distribución de juguetes en el interior
del país. Para ello cuentan con 5 depósitos distribuidos en diferentes provincias (PBA,
CABA, Chubut, Tucumán y Mendoza).
Los depósitos pueden almacenar 6 tipos diferentes de juguetes: autos, muñecas, trenes,
peluches, spinners y cartas.
La oficina central, recibe mensualmente una planilla de existencias donde se indican las
existencias de cada juguete para cada depósito.
Realizar un menú de opciones:
1. Obtener existencias: para ello deberá cargar en el main la existencia de cada juguete
en todos los depósitos. En una lista de cantidad, no uno por uno. Por lo que habrá una
matriz con 3 columnas o filas, provincia, tipo de juguete y cantidad.
2. Calcular por cada depósito la cantidad total de juguetes almacenados entre todos los
tipos.
3. Obtener los nombres de los juguetes que es necesario reponer en cada depósito.
Crear una función que devuelva todos los juguetes con menos de 500 unidades.
4. Máxima cantidad de juguetes almacenados de cada tipo. Devolver en qué provincia se
encuentran.
5. Depósito con mayor recaudación, teniendo en cuenta que disponemos de un vector
con los valores por unidad de cada juguete. Esto se debe hacer con una función que
reciba la lista de precios por parámetro para poder actualizarlos frente a la inflación.
6. Cantidad de depósitos que hayan almacenado más de 50.000 unidades entre los 6
juguetes. Mostrar provincias.
7. Porcentaje de juguetes de cada tipo sobre el total de juguetes almacenados. Realizar
una función que muestre el porcentaje de cada uno.
8. Generar un informe con la recaudación de cada depósito, ordenada de mayor a menor
usando insertion sort o quick sort. Justificar la elección del algoritmo. Para ello la
función deberá recibir una matriz de ventas, y una lista de precios.
9. Generar una función que permita corregir un error de carga mediante carga aleatoria o
distribuida de matrices.
"""
# Definimos una lista de juguetes y provincias.
juguetes = ["autos", "muñecas", "trenes", "peluches", "spinners", "cartas"]
provincias = ["PBA", "CABA", "Chubut", "Tucumán", "Mendoza"]

# Datos de existencias de juguetes en los 5 depósitos. Filas: provincias, Columnas: tipos de juguetes.
existencias = [ 
    ["PBA", "autos", 9856],
    ["PBA", "mueñecas", 44857],
    ["PBA", "cartas", 2437],
    ["CABA", "autos", 312],
    ["CABA", "muñecas", 55],
    ["CABA", "cartas", 784],
    ["Chubut", "autos", 243],
    ["Chubut", "muñecas", 342],
    ["Chubut", "cartas", 76],
    ["Tucuman", "trenes", 41],
    ["Tucuman", "cartas", 679],
    ["Tucuman", "autos", 59],
    ["Mendoza", "muñecas", 200],
    ["Mendoza", "cartas", 99],
    ["Mendoza", "autos", 208],
]

# Punto 1, Mostrar existencias.
def mostrar_existencias():
    for i in range(len(provincias)):
        print(f"\nDepósito en {provincias[i]}:")
        for j in range(len(juguetes)):
            print(f" - {juguetes[j]}: {existencias[i][j]} unidades")
    return mostrar_existencias

# Punto 2, Calcular cantidad total de juguetes por depósito.
def total_juguetes_por_deposito():
    for i in range(len(provincias)):
        total = 0
        for j in range(len(juguetes)):
            total += existencias[i][j]
        print(f"Depósito en {provincias[i]}: {total} juguetes")
    return total_juguetes_por_deposito

# Punto 3, Obtener juguetes con menos de 500 unidades por depósito.
def obtener_juguetes_reponer_deposito():
    for i in range(len(provincias)):
        print(f"\nDepósito en {provincias[i]}:")
        for j in range(len(juguetes)):
            if existencias[i][j] < 500:
                print(f" - {juguetes[j]}: {existencias[i][j]} unidades")
    return obtener_juguetes_reponer_deposito
# Punto 4, Máxima cantidad de juguetes por tipo.
def max_juguetes_por_tipo():
    for j in range(len(juguetes)):
        max_cantidad = 0
        provincia_max = ""
    for i in range(len(provincias)):
        if existencias[i][j] > max_cantidad:
            max_cantidad = existencias[i][j]
            provincia_max = provincias[i]
    print(f" - {juguetes[j]}: {max_cantidad} unidades en {provincia_max}")
    return max_juguetes_por_tipo

# Punto 5, Depósito con mayor recaudación.
def deposito_con_mayor_recaudacion(precios):
    max_recaudacion = 0
    provincia_max = ""
    for i in range(len(provincias)):
        recaudacion = 0
        for j in range(len(juguetes)):
            recaudacion += existencias[i][j] * precios[j]
        if recaudacion > max_recaudacion:
            max_recaudacion = recaudacion
            provincia_max = provincias[i]
    print(f"El depósito con mayor recaudación es {provincia_max} con un total de ${max_recaudacion}.")
    return deposito_con_mayor_recaudacion
# Punto 6, Depósitos con más de 50,000 juguetes almacenados.
def depositos_con_mas_de_50000():
    for i in range(len(provincias)):
        total = 0
        for j in range(len(juguetes)):
            total += existencias[i][j]
        if total > 50000:
            print(f" - {provincias[i]}: {total} juguetes")
    return depositos_con_mas_de_50000

# Punto 7, Porcentaje de juguetes por tipo.
def porcentaje_juguetes_por_tipo():
    total_juguetes = 0
    for i in range(len(existencias)):
        for j in range(len(existencias[i])):
            total_juguetes += existencias[i][j]
    
    for j in range(len(juguetes)):
        total_juguete = 0
        for i in range(len(provincias)):
            total_juguete += existencias[i][j]
        porcentaje = (total_juguete / total_juguetes) * 100
        print(f" - {juguetes[j]}: {porcentaje:.2f}% del total")
    
    return porcentaje_juguetes_por_tipo

# Punto 8, Generar informe de recaudación de cada deposito ordenada.
def generar_informe_recaudacion(precios):
    recaudaciones = [[provincias[i], 0] for i in range(len(provincias))]
    for i in range(len(provincias)):
        recaudacion = 0
        for j in range(len(juguetes)):
            recaudacion += existencias[i][j] * precios[j]
        recaudaciones[i][1] = recaudacion

    # Ordenar con Insertion Sort (Utilice la misma ya que es mas eficiente para poder resolver el ejercicio dado.)
    for i in range(1, len(recaudaciones)):
        clave = recaudaciones[i]
        j = i - 1
        while j >= 0 and recaudaciones[j][1] < clave[1]:
            recaudaciones[j + 1] = recaudaciones[j]
            j -= 1
        recaudaciones[j + 1] = clave
    
    print("\nRecaudación ordenada de mayor a menor:")
    for i in range(len(recaudaciones)):
        print(f" - {recaudaciones[i][0]}: ${recaudaciones[i][1]}")
    return generar_informe_recaudacion

# Punto 9. 