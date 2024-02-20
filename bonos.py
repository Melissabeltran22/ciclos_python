# Definimos el valor de los bonos segun el numero de hijos
bonos = {
    0: 20000,
    1: 25000,
    2: 25000,
    3: 30000
}

# definimos las variables para contar personas y dinero
personas_estrato1 = 0
personas_estrato2 = 0
dinero_estrato1 = 0
dinero_estrato2 = 0

# definimos las variables para contar el # de hijos
hijos_0 = 0
hijos_1_2 = 0
hijos_3_mas = 0
dinero_hijos_0 = 0
dinero_hijos_1_2 = 0
dinero_hijos_3_mas = 0

# Ciclo for para preguntar los datos
for _ in range(10):
    while True:
        estrato = int(input("Ingrese el estrato (1 o 2): ")) - 1
        if estrato in [0, 1]:
            break
        else:
            print("Selecciona 1 o 2 según tu estrato")

    num_hijos = int(input("Ingrese el numero de hijos: "))

    #Si tiene más de 3 hijos, solo contamos 3
    if num_hijos > 3:
        num_hijos = 3

    #agregamos el estrato
    if estrato == 0:
        personas_estrato1 += 1
        dinero_estrato1 += bonos[num_hijos]
    else:
        personas_estrato2 += 1
        dinero_estrato2 += bonos[num_hijos]

    #Sumamos la infomración de hijos
    if num_hijos == 0:
        hijos_0 += 1
        dinero_hijos_0 += bonos[num_hijos]
    elif num_hijos in [1, 2]:
        hijos_1_2 += 1
        dinero_hijos_1_2 += bonos[num_hijos]
    else:
        hijos_3_mas += 1
        dinero_hijos_3_mas += bonos[num_hijos]

print("-------------------------------------------------------------------------------")
print("                 RESUMEN DE BONOS SEGÚN ESTRATO Y NÚMERO DE HIJOS              ")
print("-------------------------------------------------------------------------------")
print("Total número de personas  estrato 1: ------> ", personas_estrato1)
print("Total dinero entregado al estrato 1: ------> ", dinero_estrato1)
print("Total número de personas  estrato 2: ------> ", personas_estrato2)
print("Total dinero entregado al estrato 2: ------> ", dinero_estrato2)
print("                                                                      ")
print("Total beneficiarios sin hijos:         ------>", hijos_0,      "   ---   ", " el dinero en bonos es -------> $ ", dinero_hijos_0)
print("Total beneficiarios con 1 o 2 hijos:   ------>", hijos_1_2,    "   ---   ", " el dinero en bonos es -------> $ ", dinero_hijos_1_2)
print("Total beneficiarios con 3 o más hijos: ------>", hijos_3_mas,  "   ---   ", " el dinero en bonos es -------> $ ", dinero_hijos_3_mas)
print("                                                                      ")
#Sumamos el total de dinero y lo imprimimos
total_dinero = dinero_estrato1 + dinero_estrato2
print("TOTAL DINERO PAGADO EN BONOS: -------> $ ", total_dinero)