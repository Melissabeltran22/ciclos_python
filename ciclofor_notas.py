# imprima la tabla del 123

def CicloFor ():
    for i in range(11):
        print(f"La tabla del 123 es {i} * {i*123}")

    multiplo = int(input("Ingrese un multiplo"))
    for i in range(11):
        print(f"Tabla es = {multiplo} * {i} = {i*multiplo}")

def Ejemplo():

    aumTotal = 0
    acumVentasMenos = 0
    acumVentasMayores = 0
    contVentasMenos = 0
    contVentasMayores = 0
    print('*************** Registro de ventas ***************')
    for i in range(2):
        nombrePro = input("Producto -> ")
        precio = int(input("Precio --> "))
        cantidad = int(input("Cantidad -->"))
        subTotal = precio * cantidad
        print(f"subTotal -->{subTotal} \n")
        if(subTotal > 200000):
            contVentasMayores = contVentasMayores + 1
            acumVentasMayores = acumVentasMayores + subTotal
        else:
            contVentasMenos = contVentasMenos + 1
            acumVentasMenos = acumVentasMenos + subTotal
    aumTotal = aumTotal + subTotal
    print('________________________________________________________')
    print(f"total ventas  {aumTotal}")
    print(f"Total ventas mayores --------> {acumVentasMayores}")
    print(f"Total de ventas menores -----> {acumVentasMenos}")
    print(f"Cantidad de ventas Mayores --> {contVentasMayores}")
    print(f"Cantidad de centas manores --> {contVentasMenos}")
    print('________________________________________________________')

def Notas():
    print("Materias \n")
    print("Elije una opcion")
    print("1. Python")
    print("2. Logica")
    materia = int(input("Escribe una opción"))

    promedioNotas = float
    notas = []
    nota = 0
    gano = 3.0
    for i in range(11):
        if(materia == 1):
            nota = float(input("Ingresa la nota de Python: "))
            notas.append(nota)
        elif( materia == 2):
            nota = float(input("Ingresa la nota de Logica: "))
            notas.append(nota)
        else:
            print("ingrese una opcion valida")
            break
    if all(gano)
    print(notas)
    promedioNotas = sum(notas)
    print(notas)



if __name__ == '__main__':
    #CicloFor()
    #Ejemplo()}
    Notas()