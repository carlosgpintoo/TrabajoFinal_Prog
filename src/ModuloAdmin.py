usuarios = {"Paraisodelsol": "Programacion123"}


costos_unitarios = {
    "hab_individual": 50,
    "hab_pareja": 80,
    "hab_familia": 120,
    "comida": 20,
    "paseo": 60,
    "mascota": 40
}

precios_venta = {
    "hab_individual": 100,
    "hab_pareja": 170,
    "hab_familia": 260,
    "comida": 30,
    "paseo": 90,
    "mascota": 60
}


RECARGO_HAB = 20       
RECARGO_COMIDA = 5     #Costo para hotel si no hay servicio disponible
RECARGO_PASEO = 10     


def autenticar():
    usuario = input("Ingrese usuario: ")
    contraseña = input("Ingrese contraseña: ")

    if usuario in usuarios and usuarios[usuario] == contraseña:
        print("Bienvenido al módulo administrador.\n")
        return True
    else:
        print("Acceso denegado.\n")
        return False


def mostrar_reportes(clientes, ventas, costos, ganancia,
                     tipos_habitacion, mascotas,
                     habitaciones_disponibles,
                     alimentacion_disponible,
                     paseos_disponibles):

    print("\n********* REPORTES DEL DÍA **********")

    print(f"Total de clientes en el hotel: {len(clientes)}")

    print("\nTotal de clientes por tipo de habitación:")
    print(f"  Individual: {tipos_habitacion['individual']}")
    print(f"  Pareja:     {tipos_habitacion['pareja']}")
    print(f"  Familia:    {tipos_habitacion['familia']}")

    print(f"\nTotal de mascotas: {mascotas}")

    print("\nDisponibilidad de habitaciones:")
    print(f"  Individuales disponibles: {habitaciones_disponibles['individual']}")
    print(f"  Parejas disponibles:     {habitaciones_disponibles['pareja']}")
    print(f"  Familias disponibles:    {habitaciones_disponibles['familia']}")

    print("\nDisponibilidad de servicios:")
    print(f"  Comidas disponibles : {alimentacion_disponible}")
    print(f"  Paseos disponibles :       {paseos_disponibles}")

    print("\nResumen ganancias:")
    print(f"  Ventas totales: {ventas}")
    print(f"  Costos totales: {costos}")
    print(f"  Ganancia:       {ganancia}")

    print("***** FIN DE REPORTES *****\n")


def registrar_cliente(clientes, tipos_habitacion, mascotas,
                      habitaciones_disponibles, ventas, costos, ganancia,
                      alimentacion_disponible, paseos_disponibles):

    print("\n***** Registro de cliente *****")
    nombre = input("Nombre del cliente: ")
    tipo = input("Tipo de habitación (individual, pareja, familia): ").lower()

    if tipo not in habitaciones_disponibles:
        print("Tipo de habitación inválido.\n")
        return (clientes, tipos_habitacion, mascotas,
                habitaciones_disponibles, ventas, costos, ganancia,
                alimentacion_disponible, paseos_disponibles)

    costo_hotel = 0
    venta_cliente = 0

    if tipo == "individual":
        costo_hab = costos_unitarios["hab_individual"]
        precio_hab = precios_venta["hab_individual"]
    elif tipo == "pareja":
        costo_hab = costos_unitarios["hab_pareja"]
        precio_hab = precios_venta["hab_pareja"]
    else:
        costo_hab = costos_unitarios["hab_familia"]
        precio_hab = precios_venta["hab_familia"]

    if habitaciones_disponibles[tipo] > 0:
        habitaciones_disponibles[tipo] -= 1
    else:
        print("No habia habitacion disponible, se alistará una.")
        costo_hotel += RECARGO_HAB

    costo_hotel += costo_hab
    venta_cliente += precio_hab
    tipos_habitacion[tipo] += 1

    comidas = int(input("Comidas adicionales: "))
    paseos = int(input("Paseos adicionales: "))
    cant_mascotas = int(input("Mascotas: "))

    if comidas > 0:
        if comidas <= alimentacion_disponible:
            alimentacion_disponible -= comidas
            costo_hotel += comidas * costos_unitarios["comida"]
        else:
            normales = alimentacion_disponible
            extras = comidas - alimentacion_disponible
            alimentacion_disponible = 0

            costo_hotel += normales * costos_unitarios["comida"]
            costo_hotel += extras * (costos_unitarios["comida"] + RECARGO_COMIDA)

        venta_cliente += comidas * precios_venta["comida"]

    if paseos > 0:
        if paseos <= paseos_disponibles:
            paseos_disponibles -= paseos
            costo_hotel += paseos * costos_unitarios["paseo"]
        else:
            normales_p = paseos_disponibles
            extras_p = paseos - paseos_disponibles
            paseos_disponibles = 0

            costo_hotel += normales_p * costos_unitarios["paseo"]
            costo_hotel += extras_p * (costos_unitarios["paseo"] + RECARGO_PASEO)

        venta_cliente += paseos * precios_venta["paseo"]

    if cant_mascotas > 0:
        costo_hotel += cant_mascotas * costos_unitarios["mascota"]
        venta_cliente += cant_mascotas * precios_venta["mascota"]
        mascotas += cant_mascotas

    ventas += venta_cliente
    costos += costo_hotel
    ganancia = ventas - costos

    clientes.append(nombre)

    print("\n Cliente registrado exitosamente")
    print(f"  Venta al cliente: {venta_cliente}")
    print(f"  Costo para el hotel: {costo_hotel}")
    print(f"  Ganancia acumulada: {ganancia}\n")

    return (clientes, tipos_habitacion, mascotas,
            habitaciones_disponibles, ventas, costos, ganancia,
            alimentacion_disponible, paseos_disponibles)


def modulo_administrador():
    clientes_local = []
    tipos_local = {"individual": 0, "pareja": 0, "familia": 0}
    mascotas_local = 0
    hab_local = {"individual": 5, "pareja": 9, "familia": 12}
    ventas_local = 0
    costos_local = 0
    ganancia_local = 0
    alim_local = 100
    paseos_local = 50

    if autenticar():
        while True:
            print("**** MÓDULO ADMINISTRADOR ****")
            print("1. Ver reportes")
            print("2. Registrar un cliente")
            print("3. Salir")
            op = input("Opción: ")

            if op == "1":
                mostrar_reportes(
                    clientes_local,
                    ventas_local,
                    costos_local,
                    ganancia_local,
                    tipos_local,
                    mascotas_local,
                    hab_local,
                    alim_local,
                    paseos_local
                )

            elif op == "2":
                (clientes_local, tipos_local, mascotas_local,
                 hab_local, ventas_local, costos_local, ganancia_local,
                 alim_local, paseos_local) = registrar_cliente(
                    clientes_local, tipos_local, mascotas_local,
                    hab_local, ventas_local, costos_local, ganancia_local,
                    alim_local, paseos_local
                )

            elif op == "3":
                print("Saliendo del módulo administrador.\n")
                break

            else:
                print("Opción inválida.\n")


modulo_administrador()
