import funciones as f

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

while len(existencias) < 2:
    existencias += [f.mostrar_existencias()]

def menu():
    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Obtener existencias")
        print("2. Calcular cantidad total de juguetes por depósito")
        print("3. Obtener nombres de juguetes que es necesario reponer (menos de 500 unidades)")
        print("4. Máxima cantidad de juguetes por tipo y depósito donde se encuentra")
        print("5. Depósito con mayor recaudación")
        print("6. Depósitos con más de 50,000 juguetes almacenados")
        print("7. Porcentaje de juguetes por tipo")
        print("8. Informe de recaudación ordenada")
        print("9. Corregir error de carga")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            f.mostrar_existencias()
        elif opcion == "2":
            f.total_juguetes_por_deposito()
        elif opcion == "3":
            f.obtener_juguetes_reponer_deposito()
        elif opcion == "4":
            f.max_juguetes_por_tipo()
        elif opcion == "5":
            f.deposito_mayor_recaudacion()
        elif opcion == "6":
            f.depositos_con_mas_de_50000()
        elif opcion == "7":
            f.porcentaje_juguetes_por_tipo()
        elif opcion == "8":
            f.generar_informe_recaudacion()
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Intente nuevamente.")